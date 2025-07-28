// Dolly Robot - Arduino Motor Controller
// Handles motor control, safety systems, and USB communication with Mac Mini

#include <AccelStepper.h>
#include <Servo.h>

// Constants
#define HEARTBEAT_TIMEOUT 100  // milliseconds
#define BAUD_RATE 115200

// Motor pins (adjust for your setup)
#define BASE_MOTOR_STEP 2
#define BASE_MOTOR_DIR 3
#define ARM_MOTOR1_STEP 4
#define ARM_MOTOR1_DIR 5
#define ARM_MOTOR2_STEP 6
#define ARM_MOTOR2_DIR 7

// Safety pins
#define EMERGENCY_STOP_PIN 10
#define STATUS_LED_PIN 13

// Global variables
unsigned long lastHeartbeat = 0;
bool systemEnabled = false;

// Motor objects
AccelStepper baseMotor(AccelStepper::DRIVER, BASE_MOTOR_STEP, BASE_MOTOR_DIR);
AccelStepper armMotor1(AccelStepper::DRIVER, ARM_MOTOR1_STEP, ARM_MOTOR1_DIR);
AccelStepper armMotor2(AccelStepper::DRIVER, ARM_MOTOR2_STEP, ARM_MOTOR2_DIR);

void setup() {
  Serial.begin(BAUD_RATE);
  
  // Configure pins
  pinMode(EMERGENCY_STOP_PIN, INPUT_PULLUP);
  pinMode(STATUS_LED_PIN, OUTPUT);
  
  // Configure motors
  baseMotor.setMaxSpeed(1000);
  baseMotor.setAcceleration(500);
  armMotor1.setMaxSpeed(800);
  armMotor1.setAcceleration(400);
  armMotor2.setMaxSpeed(800);
  armMotor2.setAcceleration(400);
  
  // Initial state
  digitalWrite(STATUS_LED_PIN, LOW);
  
  Serial.println("Dolly Robot Motor Controller v1.0");
  Serial.println("Waiting for connection...");
}

void loop() {
  // Check emergency stop
  if (digitalRead(EMERGENCY_STOP_PIN) == LOW) {
    emergencyStop();
  }
  
  // Check heartbeat timeout
  if (systemEnabled && (millis() - lastHeartbeat > HEARTBEAT_TIMEOUT)) {
    Serial.println("ERROR: Heartbeat timeout!");
    safeStop();
  }
  
  // Process serial commands
  if (Serial.available()) {
    processCommand();
  }
  
  // Run motors if system is enabled
  if (systemEnabled) {
    baseMotor.run();
    armMotor1.run();
    armMotor2.run();
    digitalWrite(STATUS_LED_PIN, HIGH);
  } else {
    digitalWrite(STATUS_LED_PIN, LOW);
  }
}

void processCommand() {
  String command = Serial.readStringUntil('\n');
  command.trim();
  
  // Parse JSON-like commands
  if (command.startsWith("{")) {
    // Simple JSON parser for commands
    if (command.indexOf("\"cmd\":\"heartbeat\"") > 0) {
      lastHeartbeat = millis();
      systemEnabled = true;
      Serial.println("{\"status\":\"ok\",\"timestamp\":" + String(millis()) + "}");
    }
    else if (command.indexOf("\"cmd\":\"move\"") > 0) {
      // Extract motor and position values
      // Format: {"cmd":"move","motor":"base","pos":1000}
      handleMoveCommand(command);
    }
    else if (command.indexOf("\"cmd\":\"stop\"") > 0) {
      safeStop();
      Serial.println("{\"status\":\"stopped\"}");
    }
    else if (command.indexOf("\"cmd\":\"status\"") > 0) {
      sendStatus();
    }
  }
}

void handleMoveCommand(String command) {
  // Simple parsing - in production use ArduinoJson library
  int motorIndex = command.indexOf("\"motor\":\"");
  int posIndex = command.indexOf("\"pos\":");
  
  if (motorIndex > 0 && posIndex > 0) {
    String motorName = command.substring(motorIndex + 9, command.indexOf("\"", motorIndex + 9));
    long position = command.substring(posIndex + 6, command.indexOf("}", posIndex)).toInt();
    
    if (motorName == "base") {
      baseMotor.moveTo(position);
    } else if (motorName == "arm1") {
      armMotor1.moveTo(position);
    } else if (motorName == "arm2") {
      armMotor2.moveTo(position);
    }
    
    Serial.println("{\"status\":\"moving\",\"motor\":\"" + motorName + "\",\"target\":" + String(position) + "}");
  }
}

void sendStatus() {
  String status = "{";
  status += "\"enabled\":" + String(systemEnabled ? "true" : "false") + ",";
  status += "\"emergency_stop\":" + String(digitalRead(EMERGENCY_STOP_PIN) == LOW ? "true" : "false") + ",";
  status += "\"motors\":{";
  status += "\"base\":{\"pos\":" + String(baseMotor.currentPosition()) + ",\"target\":" + String(baseMotor.targetPosition()) + "},";
  status += "\"arm1\":{\"pos\":" + String(armMotor1.currentPosition()) + ",\"target\":" + String(armMotor1.targetPosition()) + "},";
  status += "\"arm2\":{\"pos\":" + String(armMotor2.currentPosition()) + ",\"target\":" + String(armMotor2.targetPosition()) + "}";
  status += "}}";
  
  Serial.println(status);
}

void safeStop() {
  systemEnabled = false;
  baseMotor.stop();
  armMotor1.stop();
  armMotor2.stop();
  // Run to decelerate smoothly
  while (baseMotor.isRunning() || armMotor1.isRunning() || armMotor2.isRunning()) {
    baseMotor.run();
    armMotor1.run();
    armMotor2.run();
  }
}

void emergencyStop() {
  // Immediate stop - no deceleration
  systemEnabled = false;
  baseMotor.setCurrentPosition(baseMotor.currentPosition());
  armMotor1.setCurrentPosition(armMotor1.currentPosition());
  armMotor2.setCurrentPosition(armMotor2.currentPosition());
  Serial.println("{\"error\":\"EMERGENCY_STOP\"}");
}
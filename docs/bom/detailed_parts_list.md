# Dolly Robot Parts List

## Overview
This document provides a complete parts list with sources and approximate costs for building Dolly.
Parts are organized by category with multiple supplier options.

## Quick Budget Summary
- **Structural & Mechanical**: $200-250
- **Electronics & Computing**: $250-350  
- **Power System**: $200-300
- **3D Printing Materials**: $70-95
- **Mac Mini**: $600-1200 (user provided)
- **Total (without Mac Mini)**: $720-895
- **Complete System**: $1320-2095

---

## Structural Components

### Aluminum Extrusion (2020 Profile)
**Required**: 3 meters total
- 4× 600mm (vertical posts)
- 4× 300mm (base width)
- 4× 250mm (base depth)
- 2× 200mm (cross braces)

**Sources & Prices**:
- **Amazon**: T-slot 2020, ~$15-20/meter
  - [Iverntech 2020 Extrusion](https://www.amazon.com)
  - [PZRT 2020 V-Slot](https://www.amazon.com)
- **8020.net**: Industrial grade, ~$18-25/meter
  - Part #: 2020-BLACK
- **OpenBuilds**: V-Slot option, ~$12-16/meter
  - Better for wheels/linear motion
- **Local**: Check metal suppliers, often cheaper

**Budget**: $45-75 for 3 meters

### Brackets & Connectors
**Required Quantities**:
- Corner brackets (90°): 16 pieces
- T-brackets: 8 pieces  
- End caps: 16 pieces
- T-nuts: 100 pack
- M5 bolts: 100 assorted

**Sources & Prices**:
- **Amazon Kit**: ~$40-60 complete set
  - Search "2020 extrusion bracket kit"
- **Individual**:
  - Corner brackets: $1-2 each
  - T-nuts: $10-15/100 pack
  - M5 bolt kit: $15-20

**Budget**: $50-70 total

---

## Motion Components

### Motors
**NEMA 17 Stepper Motors**
- Required: 8 motors total
- Specs: 1.8° step, 40+ N⋅cm torque

**Sources & Prices**:
- **StepperOnline**: $10-15/motor
  - Model: 17HS19-2004S1
  - Bulk discounts available
- **Amazon**: $12-18/motor
  - ELEGOO/TWOTREES brands
- **Pololu**: $15-20/motor (premium)

**Budget**: $80-120 for 8 motors

### Motor Drivers
**A4988 or DRV8825 Modules**
- Required: 8 drivers
- DRV8825 preferred (quieter)

**Sources & Prices**:
- **Amazon**: $3-5/driver
  - Often sold in 5-packs
- **Pololu**: $6-8/driver (genuine)

**Budget**: $25-40 for 8 drivers

### Bearings & Shafts
**608 Bearings** (skateboard bearings)
- Required: 20 pieces
- Available everywhere

**Sources & Prices**:
- **Amazon**: $10-15/20 pack
- **Local skate shop**: $1/bearing
- **McMaster-Carr**: $15-20 (precision)

**8mm Smooth Rods**
- Required: 4× 300mm
- Hardened steel preferred

**Sources**: 
- **Amazon**: $15-20/set
- **McMaster**: $20-25 (precision ground)

**Budget**: $30-40 total

### Wheels & Mobility
**Drive Wheels**
- 70mm diameter × 2
- 6mm bore or hub adapter

**Caster Wheels**
- Ball casters × 4
- 1" diameter

**Sources & Prices**:
- **Pololu**: $10-15/wheel
- **Amazon**: $15-20/set
- **ServoCity**: $12-18/wheel

**Budget**: $35-50 total

---

## Electronics

### Microcontrollers
**Arduino Mega 2560**
- Main controller
- Genuine or clone

**Sources & Prices**:
- **Official**: $40-45
- **Clone**: $15-20 (Amazon)
- **Adafruit**: $45 (genuine)

**Arduino Nano**
- Gripper controller
- Clone acceptable

**Sources & Prices**:
- **Amazon**: $5-10
- **AliExpress**: $3-5

**Budget**: $20-55 total

### Cameras
**USB Cameras × 2**
- Overview camera: 720p minimum
- Detail camera: 1080p preferred

**Sources & Prices**:
- **Logitech C270**: $25-30
- **Generic 1080p**: $15-25
- **Arducam**: $30-50 (better optics)

**Budget**: $40-80 total

### Sensors & Switches
**Limit Switches**
- Mechanical endstops × 8

**IMU/Accelerometer**
- MPU6050 module

**Sources & Prices**:
- **Amazon**: $15-20 (switch kit)
- **Adafruit**: $10-15 (IMU)

**Budget**: $25-35 total

### Cables & Connectors
**USB Cables**
- USB-A to USB-B × 2
- USB extension × 1
- USB 3.0 hub (powered)

**Power Cables**
- IEC inlet connector
- 12AWG wire (2 meters)
- Crimp connectors

**Sources & Prices**:
- **Amazon**: $30-40 (all cables)
- **Monoprice**: $25-35 (better quality)

**Budget**: $30-40 total

---

## Power System

### Portable Power Station
**200-300Wh Capacity Minimum**

**Recommended Models**:
- **EcoFlow River Mini** (210Wh)
  - Price: $200-250
  - Weight: 6.3 lbs
  - AC outlets: 2
  - Where: Amazon, EcoFlow.com
  
- **Jackery Explorer 240** (240Wh)
  - Price: $200-250  
  - Weight: 6.6 lbs
  - AC outlets: 1
  - Where: Amazon, Jackery.com

- **Bluetti EB3A** (268Wh)
  - Price: $250-300
  - Weight: 10 lbs
  - AC outlets: 1
  - Where: Amazon, Bluettipower.com

**Budget Option**:
- Generic brands: $150-200
- Check reviews carefully

### Motor Power Supply
**12V 5A Supply**
- For stepper motors
- Better than using Mac's USB

**Sources & Prices**:
- **Amazon**: $20-25
- **Digi-Key**: $25-30

---

## 3D Printing Materials

### Filaments Required
**PLA** (main structure)
- 2kg black/gray
- 1.75mm diameter

**TPU** (flexible parts)
- 500g for grippers
- Shore 95A hardness

**PETG** (optional, durable parts)
- 1kg for high-stress parts

**Sources & Prices**:
- **Amazon Basics PLA**: $18-22/kg
- **Prusament**: $25-30/kg (premium)
- **SUNLU**: $16-20/kg (budget)
- **NinjaTek TPU**: $30-35/500g

**Budget**: $70-95 total

---

## Heavy Duty Parts
*See `dolly_heavy_parts.py` for designs*

### Metal Plates (if not 3D printing)
**Aluminum Sheet**
- 1/4" (6mm) thickness
- 300×300mm piece

**Sources & Prices**:
- **McMaster-Carr**: $30-40
- **Local metal shop**: $20-30
- **eBay**: $25-35 (cutoffs)

### Fasteners
**Bolt Assortment**
- M3×10 to M3×30: 100 pack
- M4×10 to M4×30: 100 pack  
- M5×10 to M5×30: 100 pack
- Nyloc nuts
- Washers

**Sources & Prices**:
- **BoltDepot**: $30-40 (quality)
- **Amazon**: $20-30 (variety pack)
- **McMaster**: $40-50 (certified)

---

## Where to Save Money

### Salvage Sources
**Old Printers**: Motors, rods, bearings
**Computer PSUs**: 12V power
**Broken appliances**: Motors, sensors

### Bulk Buying
- Motors: 20% off for 10+
- Filament: Buy 5kg spools
- Fasteners: Bulk packs

### Alternative Suppliers
- **AliExpress**: 50% cheaper, 3-4 week wait
- **eBay**: Good for bearings, motors
- **Local makerspaces**: Group buys

### DIY Options
- Wind your own cables
- 3D print wheel hubs
- Make your own brackets

---

## Supplier Quick Reference

### Fast Shipping (1-2 days)
- Amazon Prime
- McMaster-Carr (same day in some areas)
- Local stores

### Best Prices (1-4 weeks)
- AliExpress
- Banggood  
- Direct from China

### Quality Parts
- Pololu (motors/electronics)
- Adafruit (electronics)
- McMaster (mechanical)
- 8020.net (extrusion)

### Maker-Friendly
- SparkFun
- SeeedStudio
- OpenBuilds
- Inventables

---

## Complete Shopping Lists

### Amazon Quick List
Search these terms for complete kits:
- "2020 extrusion kit 1000mm"
- "NEMA 17 stepper motor 8 pack"
- "Arduino Mega starter kit"
- "608 bearing 20 pack"
- "M5 bolt assortment kit"

### McMaster Part Numbers
- 47065T101: 2020 Extrusion
- 60355K503: 608 Bearings
- 1265K32: 8mm Precision Shaft
- 92855A310: M5 Socket Bolts

---

*Prices current as of 2024. Check dolly-robot.com for updated lists and community supplier recommendations.*
# Dolly Robot

> "Hello Dolly!" - An open-source modular robot with a Mac Mini brain 🤖

## 🌟 Overview

Dolly is a 2-foot tall modular robot designed for delicate tasks like circuit building, with the ability to swap into larger frames for different applications. Powered by a Mac Mini and portable solar generators, Dolly represents a new approach to accessible, repairable robotics.

https://medium.com/@mbonsign/the-3-month-gap-how-ai-went-from-drawing-dots-to-designing-robots-fe38315c959b  

## ✨ Key Features

- **Mac Mini Brain**: Full computing power in a compact robot
- **Modular Design**: Core module swaps between task-specific frames
- **Solar Generator Power**: Safe, accessible power system
- **3D Printable**: Self-repairing with standard parts
- **Delicate Manipulation**: Designed for circuit building and fine work
- **"Hello Dolly" Wake Word**: Voice-activated assistance

## 🏗️ Project Structure

```
dolly-robot/
├── hardware/        # CAD files and mechanical design
│   ├── cad/        # CADQuery source files
│   ├── stl/        # Ready-to-print files
│   └── step/       # STEP files for CAD software
├── firmware/       # Arduino/microcontroller code
│   └── arduino/    # Motor control and safety systems
├── software/       # High-level control software
│   ├── vision/     # Computer vision for component recognition
│   ├── control/    # Robot control and planning
│   └── voice/      # "Hello Dolly" wake word detection
├── docs/           # Documentation and guides
│   ├── assembly/   # Build instructions
│   ├── bom/        # Bill of materials
│   └── safety/     # Safety guidelines
└── examples/       # Example projects and demos
```

## 🚀 Getting Started

### Prerequisites

- Mac Mini (M1/M2 recommended)
- 3D Printer
- Basic electronics tools
- Aluminum extrusion (2020 profile)
- Portable power station (300Wh+)

### Quick Start

1. **Print the Parts**: Start with the core module components in `/hardware/stl/`
2. **Gather Materials**: Check the [Bill of Materials](docs/bom/README.md)
3. **Flash Firmware**: Upload Arduino code from `/firmware/arduino/`
4. **Install Software**: Set up the control system from `/software/`
5. **Assemble**: Follow the [Assembly Guide](docs/assembly/README.md)

## 🤖 Specifications

### Base Configuration (Circuit Builder)
- **Height**: 24 inches (60cm)
- **Weight**: ~15 lbs (6.8kg)
- **Power**: 200-300Wh internal, unlimited when docked
- **Reach**: 12-16 inches from center
- **Precision**: 2.54mm breadboard compatibility

### Modular Frames
- Circuit Builder Frame (default)
- House Cleaning Frame (coming soon)
- Garden Assistant Frame (planned)
- Workshop Helper Frame (planned)

## 🛠️ Hardware

### Structure
- 2020 Aluminum extrusion frame
- 3D printed joints and mounts
- Standard hardware (M3/M4/M5 bolts)

### Electronics
- Mac Mini (user provided)
- Arduino Mega (motor control)
- USB cameras for vision
- NEMA 17 stepper motors
- Standard 608 bearings

### Power System
- Portable power station (EcoFlow, Jackery, etc.)
- Hot-swappable power design
- Wall outlet compatibility
- "Belly door" USB connection

## 💻 Software

### Core Components
- **Vision System**: OpenCV for component recognition
- **Motion Planning**: ROS 2 compatible
- **Voice Control**: "Hello Dolly" activation
- **Web Interface**: Remote monitoring and control
- **Safety System**: Watchdog timers and emergency stops

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for details.

### How to Contribute
1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📜 License

This project is licensed under the MIT License for software and CERN-OHL-S v2 for hardware - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Named after Dolly (like the Dalai Lama) - a helpful, peaceful presence
- Inspired by the maker community's need for accessible robotics
- Built on the shoulders of open-source giants

## 📞 Contact

- **GitHub Issues**: [Report bugs or request features](https://github.com/yourusername/dolly-robot/issues)
- **Discussions**: [Join the community](https://github.com/yourusername/dolly-robot/discussions)

---

*"Hello Dolly!" - Let's build robots that build things!* 🛠️🤖

# Dolly Robot Parts Organization

## Overview
Dolly's parts are organized into three main categories to help builders understand what they need:

1. **Purchased Parts** - Things you buy (see `/docs/bom/detailed_parts_list.md`)
2. **Heavy Duty Parts** - Strong structural components 
3. **3D Printed Parts** - Creative, customizable components

---

## 📋 Purchased Parts Summary
*Full details in `/docs/bom/detailed_parts_list.md`*

### Quick Shopping List
- **Structure**: 2020 aluminum extrusion, brackets, bolts
- **Electronics**: Arduino, motors, drivers, sensors
- **Computing**: Mac Mini (user provided), USB hub
- **Power**: Portable power station (EcoFlow/Jackery)
- **Motion**: Bearings, rods, belts, wheels

**Budget**: $720-895 (without Mac Mini)

---

## 🔩 Heavy Duty Parts
*See `/hardware/cad/dolly_heavy_parts.py`*

These parts need strength and can be made from:
- **Best**: 6mm aluminum plate (waterjet/laser cut)
- **Good**: 8-10mm PETG (100% infill)
- **Budget**: 10mm PLA (100% infill, less durable)

### Parts List
1. **Main Base Plate** - Holds everything together
2. **Motor Mount Plates** - NEMA 17 mounts (8 needed)
3. **Mac Mini Security Plate** - Anti-vibration mount
4. **Power Station Bracket** - Universal holder
5. **Arm Base Joints** - Shoulder attachments (2 needed)
6. **Emergency Stop Mount** - Safety first!

### Manufacturing Options
- **Maker Space**: Many have laser cutters for aluminum
- **SendCutSend**: Online service, ~$100-150 for all parts
- **Local Shop**: Machine shops can cut from your files
- **3D Print**: Possible but use thick walls and 100% infill

---

## 🎨 3D Printed Parts
*See `/hardware/cad/dolly_3d_parts.py`*

This is where you get creative! All parts are designed to be customized.

### Categories

#### Personality Shells
Make Dolly look however you want:
- **Classic** - 1950s robot aesthetic
- **Friendly** - WALL-E inspired
- **Industrial** - Functional design
- **Retro Futuristic** - Art deco style
- **Your Design** - Make your own!

#### Functional Parts
Essential printed components:
- Cable chain links
- Encoder wheels
- Sensor mounts
- Wire guides
- Button bezels

#### Gripper Designs
Different fingers for different tasks:
- **Circuit Fingers** - Narrow tips for components
- **Soft Fingers** - TPU for delicate items
- **Your Design** - Task-specific grippers

#### Tool Attachments
Quick-change tools:
- Vacuum pickup
- Pen holder
- Camera gimbal
- Probe holder
- Your ideas!

#### Decorative Elements
Personalization options:
- LED ring mounts
- Nameplates
- Bow ties
- Hats
- Googly eyes?

### Printing Guidelines

#### Material Choice
- **PLA**: Default for most parts
- **PETG**: Structural/outdoor parts
- **TPU**: Flexible grippers and bumpers
- **ABS**: If you need chemical resistance

#### Print Settings
```
Standard Parts:
- Layer Height: 0.2mm
- Infill: 20-40%
- Supports: As needed
- Print Speed: 50mm/s

Detailed Parts:
- Layer Height: 0.1mm
- Infill: 40-60%
- Supports: Tree supports
- Print Speed: 40mm/s

Flexible Parts (TPU):
- Layer Height: 0.2mm
- Infill: 20-30%
- Print Speed: 20-30mm/s
- Retraction: Minimal
```

---

## 🛠️ Assembly Order

### Phase 1: Frame
1. Cut aluminum extrusion to length
2. Print or cut base plate
3. Assemble frame with brackets
4. Test fit Mac Mini and power station

### Phase 2: Motion
1. Install motors on mounts
2. Add wheels and bearings
3. Set up drive system
4. Test basic movement

### Phase 3: Electronics
1. Mount Arduino and drivers
2. Wire motors and power
3. Add emergency stop
4. Test with simple code

### Phase 4: Personality
1. Print your chosen head design
2. Add grippers and tools
3. Install cameras and sensors
4. Customize appearance

### Phase 5: Integration
1. Connect Mac Mini
2. Set up software
3. Calibrate systems
4. "Hello Dolly!"

---

## 🎯 Customization Ideas

### Make Dolly Yours
- **Star Wars Fan?** Design an R2-D2 or BB-8 shell
- **Steampunk?** Add brass fittings and gears
- **Minimalist?** Clean lines and hidden wires
- **Kawaii?** Big eyes and pastel colors
- **Professional?** Company colors and logo

### Functional Mods
- **Extra Arms** for more complex tasks
- **Tool Carousel** for automatic tool changes
- **Larger Wheels** for outdoor use
- **Solar Panel Hat** for extended runtime

### Share Your Designs!
The best part of open source is the community. When you create custom parts:
1. Upload STLs to the repository
2. Include your CADQuery source
3. Add photos to the gallery
4. Share on social media with #DollyRobot

---

## 📦 Part Files Location

```
dolly-robot/
├── hardware/
│   ├── cad/                    # CADQuery source files
│   │   ├── dolly_heavy_parts.py   # Structural parts
│   │   ├── dolly_3d_parts.py      # Printable parts
│   │   └── ...
│   ├── stl/                    # Ready to print
│   │   ├── heavy_parts/        # Strong parts
│   │   ├── 3d_parts/           # Organized by type
│   │   └── community/          # User submissions
│   └── step/                   # For CAD software
└── docs/
    └── bom/
        └── detailed_parts_list.md  # Shopping list
```

---

*Remember: Dolly is designed to be modified. Don't be afraid to experiment!*
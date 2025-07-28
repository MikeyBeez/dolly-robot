# Dolly Robot CAD Files

This directory contains all CADQuery source files for the Dolly robot.

## Main Assembly Files

### 🤖 `dolly_assembly.py`
**Complete robot visualization** - Shows the entire Dolly robot assembled
- Simplified representation of all major components
- Good for understanding overall proportions
- Exports: `dolly_complete_assembly.step` and `.stl`

### 🏗️ `dolly_frame_structure.py`  
**Frame only** - Just the aluminum extrusion skeleton
- Shows 2020 aluminum extrusion layout
- Includes mounting plates version
- Exports: `dolly_frame_only.step` and `dolly_frame_with_plates.step`

## Detailed Component Files

### 📦 `dolly_frame.py`
**Detailed frame components** - Individual parts for the frame
- Base plate with motor mounts
- Mac Mini mounting bracket
- Power station bay
- Belly door with USB access
- Cable reel mechanism

### 🦾 `dolly_gripper.py` (coming soon)
**Gripper assembly** - Delicate manipulation system
- Parametric finger design
- TPU compliant tips
- Quick-change mounting

### 🔧 `dolly_arms.py` (coming soon)
**Arm mechanisms** - 6DOF manipulator arms
- Shoulder, elbow, wrist joints
- Belt and pulley layouts
- Wire management

## How to Use These Files

1. **Quick Visualization**: Start with `dolly_assembly.py` to see the whole robot
2. **Frame Building**: Use `dolly_frame_structure.py` for cutting list and assembly
3. **Detailed Parts**: Reference component files for 3D printing individual parts

## Generating Files

```bash
# Generate all STEP and STL files
python dolly_assembly.py
python dolly_frame_structure.py
python dolly_frame.py
```

## File Relationships

```
dolly_assembly.py (overview)
    ├── References simplified versions of all components
    ├── Shows spatial relationships
    └── Not for manufacturing - just visualization

dolly_frame_structure.py (skeleton)
    ├── Exact frame dimensions
    ├── Extrusion cut list
    └── Mounting plate locations

dolly_frame.py (detailed parts)
    ├── Individual 3D printable components
    ├── Parametric - can be customized
    └── Manufacturing-ready files
```

## Customization

All files use parametric design. Key parameters:
- Robot height: 610mm (24")
- Base dimensions: 300mm × 250mm
- Extrusion: 2020 aluminum
- Mac Mini space: 197mm × 197mm × 36mm

Modify class `__init__` methods to adjust dimensions.

## Next Steps

1. Run the Python files to generate STEP/STL files
2. Review in your CAD software
3. Adjust parameters as needed
4. Start with frame assembly
5. Print components as you go

Remember: This is an open-source project - improvements welcome!
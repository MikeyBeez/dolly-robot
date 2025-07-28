# Viewing Dolly Robot 3D Models

## The Current Situation

The Dolly Robot project includes CADQuery Python scripts that **generate** STEP files, but these files don't exist yet in the repository. You need to:

1. **First generate the files** by running the CADQuery scripts
2. **Then view them** using one of many available viewers

## Quick Start

### Step 1: Generate STEP Files

```bash
# Make sure you have CADQuery installed
pip install cadquery

# Generate the STEP files
cd hardware/cad
python dolly_assembly.py
python dolly_frame_structure.py
python dolly_heavy_parts.py
python dolly_3d_parts.py
```

### Step 2: View the Files

Run our viewer helper:
```bash
python view_step_files.py
```

Or manually use one of these options:

## Viewing Options

### 🌐 Online Viewers (No Install Needed)

1. **[Autodesk Viewer](https://viewer.autodesk.com/)**
   - Best for: Professional viewing with measurements
   - Just drag & drop your STEP file
   - Free, no registration

2. **[ShareCAD](https://www.sharecad.org/cadframe/load)**
   - Best for: Quick viewing
   - Simple interface
   - Can share links

3. **[3DViewer.net](https://3dviewer.net/)**
   - Best for: Modern UI
   - Good performance
   - Multiple format support

### 💻 Desktop Software (Free)

1. **FreeCAD**
   ```bash
   # Install
   brew install freecad  # macOS
   sudo apt-get install freecad  # Linux
   
   # Open file
   freecad dolly_complete_assembly.step
   ```

2. **OpenSCAD**
   ```bash
   # Install
   brew install openscad
   
   # View (create a .scad file):
   import("dolly_complete_assembly.step");
   ```

3. **Fusion 360** (Free for personal use)
   - Download from Autodesk
   - Full CAD capabilities

## What You'll See

Once generated, the main files are:

- `dolly_complete_assembly.step` - The full robot
- `dolly_frame_only.step` - Just the aluminum frame
- `dolly_main_base_plate.step` - The base with motor mounts
- `dolly_mac_mini_mount.step` - Mac Mini bracket
- Various gripper and tool designs

## Why STEP Files?

STEP files preserve exact geometry and can be:
- Edited in CAD software
- Converted to STL for 3D printing  
- Used for manufacturing
- Shared with anyone using CAD

## Troubleshooting

**"No STEP files found"**
- You need to run the Python scripts first to generate them

**"Can't install CADQuery"**
- Try: `pip install cadquery==2.1`
- Or use conda: `conda install -c cadquery -c conda-forge cadquery`

**"Online viewer won't load"**
- File might be too large (>25MB)
- Try a different viewer
- Use desktop software instead

## Alternative: Pre-Generated Files

If you can't run CADQuery, you could:
1. Ask someone to generate and share the STEP files
2. Use the STL files (if available) instead
3. Work from the technical drawings in the docs

---

The 3D models exist as code - they just need to be "compiled" into STEP files first!
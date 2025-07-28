# CADQuery Export Formats Guide

## Overview

CADQuery can export to multiple formats, each suited for different purposes. This means you can view Dolly's designs without needing special CAD software!

## Supported Export Formats

### 🌐 Browser-Viewable (No Software Needed!)

#### **SVG** - Scalable Vector Graphics
- **View in**: Any web browser, no installation needed!
- **Best for**: Documentation, technical drawings, sharing
- **Features**: Clean 2D projections, vector format, editable
```python
cq.exporters.export(obj, "part.svg", opt={
    "projectionDir": (1, 0, 0),  # Front view
    "width": 800,
    "height": 600
})
```

#### **VRML** (.wrl) - Virtual Reality Modeling Language  
- **View in**: Many browsers with VRML plugin, Blender
- **Best for**: 3D visualization with colors
- **Features**: Lightweight 3D format, color support

### 🖨️ 3D Printing Formats

#### **STL** - Standard Tessellation Language
- **View in**: Any 3D printing slicer, Windows 10 3D Viewer, many online viewers
- **Best for**: 3D printing
- **Features**: Universal mesh format
```python
cq.exporters.export(obj, "part.stl", tolerance=0.001)
```

#### **AMF** - Additive Manufacturing Format
- **View in**: Modern slicers, some CAD software
- **Best for**: Advanced 3D printing with colors/materials
- **Features**: Next-gen 3D printing format

### 🔧 CAD Exchange Formats

#### **STEP** - Standard for Exchange of Product Data
- **View in**: FreeCAD, Fusion 360, online CAD viewers
- **Best for**: Full CAD data exchange
- **Features**: Preserves exact geometry

#### **DXF** - Drawing Exchange Format
- **View in**: LibreCAD (free), AutoCAD, online viewers
- **Best for**: 2D profiles, laser cutting
- **Features**: 2D vector format

### 🎮 3D Visualization

#### **Three.js JSON**
- **View in**: Web browsers with Three.js
- **Best for**: Interactive web 3D
- **Features**: Web-ready 3D format

## Quick Export Examples

### Export Everything at Once
```python
import cadquery as cq

# Create your part
part = cq.Workplane("XY").box(100, 50, 30)

# Export to all major formats
formats = {
    'step': 'hardware/step/part.step',
    'stl': 'hardware/stl/part.stl', 
    'svg': 'hardware/svg/part.svg',
    'dxf': 'hardware/dxf/part.dxf',
    'vrml': 'hardware/vrml/part.wrl'
}

for fmt, path in formats.items():
    cq.exporters.export(part, path)
```

### Generate Multiple Views as SVG
```python
views = [
    ('top', (0, 0, 1)),
    ('front', (1, 0, 0)),
    ('side', (0, 1, 0)),
    ('isometric', (1, 1, 1))
]

for name, direction in views:
    cq.exporters.export(
        part,
        f'part_{name}.svg',
        opt={"projectionDir": direction}
    )
```

## Viewing Without CAD Software

### Option 1: SVG Files (Easiest!)
1. Generate SVG files from CADQuery
2. **Open in any web browser** - that's it!
3. Can zoom, pan, print directly

### Option 2: STL Files  
1. Generate STL files
2. View options:
   - Windows 10: Built-in 3D Viewer
   - Online: [viewstl.com](https://www.viewstl.com/)
   - Any 3D printing slicer

### Option 3: HTML Gallery
We've created `svg-viewer.html` that displays all SVG exports in a nice gallery format.

## Running the Exporters

### Export All Dolly Parts
```bash
cd hardware/cad

# Run the multi-format exporter
python multi_format_export.py

# Or export individual files
python dolly_assembly.py        # Now exports STEP, STL, and SVG
python dolly_frame_structure.py # Same - multiple formats
```

### View the Results
```bash
# Open SVG files in browser (macOS example)
open hardware/svg/dolly_assembly_top.svg

# Open the SVG gallery
open docs/svg-viewer.html

# View STL files online
# Just drag STL files to viewstl.com
```

## File Size Comparison

Typical file sizes for a medium-complexity part:
- **SVG**: 50-200 KB (tiny, vector graphics)
- **DXF**: 100-500 KB (2D profiles only)
- **STL**: 1-10 MB (mesh density dependent)
- **VRML**: 2-15 MB (includes color data)
- **STEP**: 500 KB - 5 MB (exact geometry)
- **AMF**: 1-8 MB (compressed XML)

## Why This Matters

Instead of requiring expensive CAD software, you can:
1. Generate parts with CADQuery (Python code)
2. Export to SVG for instant browser viewing
3. Share STL files that anyone can view
4. Provide STEP files for those who need to edit

This makes Dolly truly accessible - anyone can view the designs, even without CAD software!

## Troubleshooting

**"SVG is blank"**
- Check the projectionDir - you might be looking at an edge
- Try different views (top, front, side)

**"STL won't load"**
- File might be too large for online viewers
- Try a desktop viewer or reduce mesh quality

**"DXF export fails"**
- DXF only works for 2D profiles
- Select a specific face before exporting

**"Can't install CADQuery"**
- Try: `conda install -c cadquery -c conda-forge cadquery`
- Or use the CQ-editor AppImage (includes everything)
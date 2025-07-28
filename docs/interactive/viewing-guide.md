# Viewing 3D Models

## Quick Start

1. **Generate STEP Files**
   ```bash
   cd hardware/cad
   python dolly_assembly.py
   python dolly_frame_structure.py
   python dolly_frame.py
   python dolly_heavy_parts.py
   python dolly_3d_parts.py
   ```

2. **View Locally**
   - Open `/docs/interactive/3d-viewer.html` in your browser
   - Files need to be on GitHub for embedded viewer to work

3. **Upload to GitHub**
   ```bash
   git add hardware/step/*.step
   git commit -m "Add generated STEP files"
   git push
   ```

## Using 3DViewer.net

The interactive documentation uses 3DViewer.net to display STEP files directly in the browser.

### Method 1: Embedded Viewer (Recommended)
- Files must be accessible via URL (GitHub raw URLs work)
- Open `3d-viewer.html` after files are on GitHub
- Click buttons to load different models

### Method 2: Direct Upload
1. Go to https://3dviewer.net
2. Drag and drop your STEP file
3. Use mouse to navigate:
   - Left click + drag: Rotate
   - Right click + drag: Pan
   - Scroll: Zoom

### Method 3: URL Parameter
```
https://3dviewer.net#model=https://raw.githubusercontent.com/YourUsername/dolly-robot/master/hardware/step/dolly_complete_assembly.step
```

## Alternative Viewers

### ShareCAD (No Account Needed)
- Visit https://sharecad.org
- Upload STEP file
- Provides measurement tools

### Autodesk Viewer (Free Account)
- Visit https://viewer.autodesk.com
- Better for detailed analysis
- Supports sectioning and measurements

### FreeCAD (Desktop)
- Open source CAD software
- Can edit STEP files
- Export technical drawings to PDF

## Creating PDF Documentation

Using FreeCAD:
```python
import FreeCAD
import importSVG

# Load STEP file
doc = FreeCAD.open("dolly_complete_assembly.step")

# Create drawing
page = doc.addObject('Drawing::FeaturePage','Page')
page.Template = 'A3_Landscape.svg'

# Add views
view = doc.addObject('Drawing::FeatureViewPart','View')
view.Source = doc.Objects[0]
view.Direction = (0,0,1)  # Top view
view.Scale = 0.1
page.addObject(view)

# Export PDF
importSVG.export([page], "dolly_assembly.pdf")
```

## Generating Screenshots

For static documentation:

1. **Using OpenSCAD**
   ```
   openscad dolly_assembly.scad --camera=0,0,0,55,0,25,500 -o assembly.png
   ```

2. **Using FreeCAD Python**
   ```python
   Gui.activeDocument().activeView().viewIsometric()
   Gui.activeDocument().activeView().fitAll()
   Gui.activeDocument().activeView().saveImage('assembly.png',1920,1080,'White')
   ```

## Tips

- STEP files preserve exact geometry
- STL files are better for 3D printing
- Use STEP for documentation and sharing
- Most viewers support measuring features
- Some viewers can show assembly animations
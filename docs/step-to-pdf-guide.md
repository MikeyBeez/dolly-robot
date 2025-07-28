# STEP to PDF Conversion Guide

## Available Solutions

### 1. FreeCAD (Recommended - Free & Open Source)

**Installation:**
```bash
# macOS
brew install freecad

# Linux
sudo apt-get install freecad

# Windows
# Download from https://www.freecadweb.org/
```

**Usage:**
```bash
# Run the converter script
freecad -c hardware/cad/step_to_pdf.py

# Or use FreeCAD GUI:
# 1. Open FreeCAD
# 2. File > Import > Select STEP file
# 3. Switch to "Drawing Workbench"
# 4. Create new A3 page
# 5. Add views (front, top, iso)
# 6. Export as PDF
```

### 2. OpenSCAD (Alternative - Free)

```bash
# Install OpenSCAD
brew install openscad  # macOS

# Convert STEP to PDF
openscad -o output.pdf -D 'import("file.step")' --export-format=pdf
```

### 3. Online Converters (Quick & Easy)

- **GreenToken**: https://www.greentoken.de/onlineconv/
  - Upload STEP → Select PDF → Download
  - Free, no registration

- **CAD Exchanger**: https://cadexchanger.com/
  - More features, requires free account
  - Better quality output

- **Convertio**: https://convertio.co/step-pdf/
  - Simple drag & drop
  - Limited file size for free

### 4. Python Libraries

**Using pythonOCC + reportlab:**
```python
from OCC.Core.STEPControl import STEPControl_Reader
from OCC.Core.BRepMesh import BRepMesh_IncrementalMesh
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A3

# Read STEP file
reader = STEPControl_Reader()
reader.ReadFile("part.step")
reader.TransferRoots()
shape = reader.OneShape()

# Create PDF with views
c = canvas.Canvas("output.pdf", pagesize=A3)
# ... add technical drawings
c.save()
```

### 5. Commercial Options

- **eDrawings** (Free viewer, paid PDF export)
- **Autodesk Viewer** (Free online, print to PDF)
- **SolidWorks** (If you have access)
- **Fusion 360** (Free for personal use)

## Creating a PDF Flipbook

### Method 1: Automated Script
```bash
#!/bin/bash
# Generate all PDFs
for step in hardware/step/*.step; do
    base=$(basename "$step" .step)
    freecad -c -u step_to_pdf.py "$step" "docs/pdf/$base.pdf"
done

# Combine into single PDF
pdfunite docs/pdf/*.pdf docs/DollyRobot_Complete.pdf
```

### Method 2: HTML to PDF
1. Generate screenshots of each part
2. Create HTML catalog
3. Print to PDF from browser
4. Result: Flipbook-style documentation

### Method 3: Markdown + Pandoc
```bash
# Create markdown with images
pandoc parts_catalog.md -o parts_catalog.pdf \
    --pdf-engine=xelatex \
    --template=technical.tex
```

## Quick Solution for Dolly

Since you want a flipbook-style PDF:

1. **Use the HTML catalog approach:**
   ```bash
   # Open in browser
   open docs/parts_catalog.html
   
   # Print to PDF (Cmd+P)
   # Select "Save as PDF"
   # Choose A3 or Letter size
   ```

2. **Or use online converter:**
   - Upload STEP files to https://www.greentoken.de/onlineconv/
   - Download PDFs
   - Combine with Preview (Mac) or pdftk

3. **Best quality:**
   - Install FreeCAD
   - Run step_to_pdf.py
   - Creates proper technical drawings

## Example Output Structure

```
docs/pdf/
├── 00_cover_page.pdf
├── 01_complete_assembly.pdf
├── 02_exploded_view.pdf
├── 03_frame_structure.pdf
├── 04_base_plate.pdf
├── 05_mac_mini_mount.pdf
├── 06_grippers.pdf
└── DollyRobot_Complete.pdf (combined)
```

Each PDF contains:
- Multiple views (front, top, side, isometric)
- Dimensions and annotations
- Material specifications
- Assembly notes
- Tactile feature callouts
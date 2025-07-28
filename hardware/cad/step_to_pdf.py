#!/usr/bin/env python3
"""
Dolly Robot - Generate PDF Documentation from STEP files
Uses FreeCAD's Python API to create technical drawings
"""

import os
import sys

# This script requires FreeCAD to be installed
# On Mac: brew install freecad
# On Linux: apt-get install freecad
# On Windows: Download from freecad.org

try:
    import FreeCAD
    import Part
    import Drawing
    import FreeCADGui
except ImportError:
    print("ERROR: FreeCAD Python modules not found!")
    print("\nTo use this script, you need FreeCAD installed.")
    print("You can also run this script from within FreeCAD's Python console.")
    sys.exit(1)

class StepToPdfConverter:
    """Convert STEP files to PDF technical drawings"""
    
    def __init__(self, step_dir="hardware/step", output_dir="docs/pdf"):
        self.step_dir = step_dir
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)
        
    def convert_step_to_pdf(self, step_file, pdf_name=None):
        """Convert a single STEP file to PDF with multiple views"""
        if pdf_name is None:
            pdf_name = os.path.splitext(os.path.basename(step_file))[0] + ".pdf"
            
        print(f"Converting {step_file} to {pdf_name}...")
        
        # Create new document
        doc = FreeCAD.newDocument("temp")
        
        # Import STEP file
        Part.insert(step_file, doc.Name)
        
        # Create drawing page
        page = doc.addObject('Drawing::FeaturePage', 'Page')
        page.Template = self.get_template_path()
        
        # Get the imported object
        obj = doc.Objects[-1]  # Last imported object
        
        # Create multiple views
        views = [
            ("FrontView", (0, 1, 0), 100, 200),    # Front view
            ("TopView", (0, 0, 1), 280, 200),      # Top view  
            ("RightView", (1, 0, 0), 100, 100),    # Right view
            ("IsoView", (1, 1, 1), 280, 100),      # Isometric view
        ]
        
        for view_name, direction, x, y in views:
            view = doc.addObject('Drawing::FeatureViewPart', view_name)
            view.Source = obj
            view.Direction = direction
            view.X = x
            view.Y = y
            view.Scale = 0.1  # Adjust based on part size
            page.addObject(view)
        
        # Add title block information
        self.add_title_block(page, os.path.basename(step_file))
        
        # Export to PDF
        output_path = os.path.join(self.output_dir, pdf_name)
        page.ViewObject.exportPdf(output_path)
        
        # Clean up
        FreeCAD.closeDocument(doc.Name)
        
        print(f"  ✓ Saved to {output_path}")
        return output_path
    
    def get_template_path(self):
        """Get the path to drawing template"""
        # Try to find FreeCAD's template directory
        template_dirs = [
            "/usr/share/freecad/Mod/Drawing/Templates",
            "/usr/local/share/freecad/Mod/Drawing/Templates",
            "C:/Program Files/FreeCAD/data/Mod/Drawing/Templates",
            "/Applications/FreeCAD.app/Contents/Resources/data/Mod/Drawing/Templates"
        ]
        
        template_name = "A3_Landscape.svg"
        
        for dir in template_dirs:
            template_path = os.path.join(dir, template_name)
            if os.path.exists(template_path):
                return template_path
                
        # If not found, create a simple template
        return self.create_simple_template()
    
    def create_simple_template(self):
        """Create a simple A3 drawing template"""
        template = '''<?xml version="1.0" encoding="UTF-8"?>
<svg width="420mm" height="297mm" viewBox="0 0 420 297">
  <rect x="10" y="10" width="400" height="277" fill="none" stroke="black" stroke-width="0.5"/>
  <rect x="290" y="247" width="120" height="40" fill="none" stroke="black" stroke-width="0.5"/>
  <text x="295" y="257" font-family="Arial" font-size="3">Title:</text>
  <text x="295" y="267" font-family="Arial" font-size="3">Part:</text>
  <text x="295" y="277" font-family="Arial" font-size="3">Date:</text>
  <text x="295" y="287" font-family="Arial" font-size="3">Scale:</text>
</svg>'''
        
        template_path = os.path.join(self.output_dir, "template.svg")
        with open(template_path, 'w') as f:
            f.write(template)
        return template_path
    
    def add_title_block(self, page, filename):
        """Add title block information to the drawing"""
        # This would add text to the title block
        # Implementation depends on FreeCAD version
        pass
    
    def convert_all_step_files(self):
        """Convert all STEP files in the directory"""
        step_files = []
        
        # Find all STEP files recursively
        for root, dirs, files in os.walk(self.step_dir):
            for file in files:
                if file.endswith('.step') or file.endswith('.STEP'):
                    step_files.append(os.path.join(root, file))
        
        print(f"Found {len(step_files)} STEP files to convert")
        
        for step_file in step_files:
            try:
                self.convert_step_to_pdf(step_file)
            except Exception as e:
                print(f"  ✗ Error converting {step_file}: {e}")
                
        print(f"\nConversion complete! PDFs saved to {self.output_dir}")

# Alternative: Command-line conversion using OpenSCAD
def create_openscad_converter():
    """Create an OpenSCAD script for STEP to PDF conversion"""
    script = '''
// OpenSCAD script to import and display STEP files
// Run with: openscad -o output.pdf --export-format=pdf input.scad

// Import the STEP file (change this path)
import("dolly_complete_assembly.step");

// You can also create multiple views:
// projection(cut=true) import("file.step"); // 2D projection

// Camera settings for different views
// --camera=eyex,eyey,eyez,centerx,centery,centerz,distance
// Front: --camera=0,-1,0,0,0,0,500
// Top: --camera=0,0,1,0,0,0,500
// Iso: --camera=1,1,1,0,0,0,500
'''
    
    with open("convert_step.scad", 'w') as f:
        f.write(script)
    
    print("Created convert_step.scad")
    print("Usage: openscad -o output.pdf convert_step.scad")

# Simpler approach: Generate HTML with screenshots
def create_html_catalog():
    """Create an HTML catalog that could be printed to PDF"""
    html = '''<!DOCTYPE html>
<html>
<head>
    <title>Dolly Robot Parts Catalog</title>
    <style>
        @media print {
            .page-break { page-break-after: always; }
        }
        body { 
            font-family: Arial, sans-serif; 
            max-width: 800px; 
            margin: 0 auto;
        }
        .part {
            margin-bottom: 2em;
            border: 1px solid #ccc;
            padding: 1em;
        }
        .views {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 1em;
        }
        .view {
            border: 1px solid #ddd;
            padding: 0.5em;
            text-align: center;
        }
        h1 { color: #333; }
        h2 { color: #0099cc; }
        .specs {
            background: #f0f0f0;
            padding: 0.5em;
            margin-top: 1em;
        }
    </style>
</head>
<body>
    <h1>Dolly Robot Technical Documentation</h1>
    <p>Generated from STEP files</p>
    
    <div class="part">
        <h2>Complete Assembly</h2>
        <div class="views">
            <div class="view">
                <h3>Front View</h3>
                <div style="width: 300px; height: 300px; background: #eee; display: flex; align-items: center; justify-content: center;">
                    [Screenshot would go here]
                </div>
            </div>
            <div class="view">
                <h3>Isometric View</h3>
                <div style="width: 300px; height: 300px; background: #eee; display: flex; align-items: center; justify-content: center;">
                    [Screenshot would go here]
                </div>
            </div>
        </div>
        <div class="specs">
            <h3>Specifications</h3>
            <ul>
                <li>Height: 610mm (24")</li>
                <li>Base: 300 x 250mm</li>
                <li>Weight: ~15 lbs</li>
                <li>Material: 2020 Aluminum + 3D Printed Parts</li>
            </ul>
        </div>
    </div>
    
    <div class="page-break"></div>
    
    <div class="part">
        <h2>Base Plate</h2>
        <div class="views">
            <div class="view">
                <h3>Top View</h3>
                <div style="width: 300px; height: 300px; background: #eee; display: flex; align-items: center; justify-content: center;">
                    [Screenshot would go here]
                </div>
            </div>
            <div class="view">
                <h3>Detail View</h3>
                <div style="width: 300px; height: 300px; background: #eee; display: flex; align-items: center; justify-content: center;">
                    [Screenshot would go here]
                </div>
            </div>
        </div>
        <div class="specs">
            <h3>Specifications</h3>
            <ul>
                <li>Material: 6mm Aluminum</li>
                <li>Size: 280 x 230mm</li>
                <li>Motor Slots: Adjustable</li>
                <li>Tactile Features: 3 dots indicate front</li>
            </ul>
        </div>
    </div>
</body>
</html>'''
    
    with open("docs/parts_catalog.html", 'w') as f:
        f.write(html)
    
    print("Created parts_catalog.html")
    print("This can be printed to PDF from any browser")

if __name__ == "__main__":
    print("STEP to PDF Conversion Options")
    print("=" * 50)
    
    # Check if running inside FreeCAD
    if "FreeCAD" in sys.modules:
        print("Running inside FreeCAD - starting conversion...")
        converter = StepToPdfConverter()
        converter.convert_all_step_files()
    else:
        print("\nOption 1: FreeCAD Python")
        print("  Run this script from FreeCAD's Python console")
        print("  Or install FreeCAD and run: freecad -c step_to_pdf.py")
        
        print("\nOption 2: OpenSCAD")
        create_openscad_converter()
        
        print("\nOption 3: HTML Catalog")
        create_html_catalog()
        
        print("\nOption 4: Online Converters")
        print("  - https://www.greentoken.de/onlineconv/")
        print("  - https://cadexchanger.com/")
        print("  - https://www.convertio.co/step-pdf/")
        
        print("\nOption 5: Command Line Tools")
        print("  - step2pdf (Linux package)")
        print("  - python-occ with reportlab")

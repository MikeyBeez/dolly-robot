#!/usr/bin/env python3
"""
Dolly Robot - Multi-Format Exporter
Export CADQuery models to various formats for different uses
"""

import cadquery as cq
from pathlib import Path
import os

class DollyExporter:
    """Export Dolly parts to multiple formats"""
    
    def __init__(self):
        # Create output directories
        self.formats = {
            'step': 'STEP files for CAD software',
            'stl': 'STL files for 3D printing',
            'svg': 'SVG drawings for documentation',
            'dxf': 'DXF files for laser cutting',
            'vrml': 'VRML for 3D visualization',
            'amf': 'AMF for advanced 3D printing',
            'json': 'Three.js JSON format',
            'png': 'PNG images for documentation'
        }
        
        for fmt in self.formats:
            Path(f'hardware/{fmt}').mkdir(parents=True, exist_ok=True)
    
    def export_all_formats(self, obj, name, formats=None):
        """Export a CadQuery object to multiple formats"""
        if formats is None:
            formats = ['step', 'stl', 'svg']  # Default formats
        
        exported = []
        
        for fmt in formats:
            if fmt == 'step':
                path = f'hardware/step/{name}.step'
                cq.exporters.export(obj, path)
                exported.append(path)
                
            elif fmt == 'stl':
                path = f'hardware/stl/{name}.stl'
                cq.exporters.export(obj, path, tolerance=0.001)
                exported.append(path)
                
            elif fmt == 'svg':
                # Export multiple views as SVG
                views = [
                    ('top', (0, 0, 1)),
                    ('front', (1, 0, 0)),
                    ('side', (0, 1, 0))
                ]
                for view_name, direction in views:
                    path = f'hardware/svg/{name}_{view_name}.svg'
                    cq.exporters.export(
                        obj,
                        path,
                        opt={
                            "projectionDir": direction,
                            "width": 800,
                            "height": 600,
                            "marginLeft": 50,
                            "marginTop": 50,
                            "showAxes": False,
                            "showHidden": False
                        }
                    )
                    exported.append(path)
                    
            elif fmt == 'dxf':
                # Export for laser cutting (2D projection)
                try:
                    path = f'hardware/dxf/{name}.dxf'
                    # Get the top face and export as DXF
                    top_face = obj.faces(">Z").val()
                    cq.exporters.export(top_face, path)
                    exported.append(path)
                except:
                    print(f"  ⚠️  Could not export DXF for {name}")
                    
            elif fmt == 'vrml':
                path = f'hardware/vrml/{name}.wrl'
                cq.exporters.export(obj, path)
                exported.append(path)
                
            elif fmt == 'amf':
                path = f'hardware/amf/{name}.amf'
                cq.exporters.export(obj, path)
                exported.append(path)
                
            elif fmt == 'json':
                # Three.js JSON format
                path = f'hardware/json/{name}.json'
                cq.exporters.export(obj, path)
                exported.append(path)
        
        return exported

# Example: Create and export a simple part in multiple formats
def demo_multi_export():
    """Demonstrate multi-format export"""
    print("CadQuery Multi-Format Export Demo")
    print("=" * 50)
    
    # Create a simple part
    print("\nCreating demo part...")
    demo_part = (
        cq.Workplane("XY")
        .box(100, 80, 20)
        .edges("|Z").fillet(5)
        .faces(">Z").workplane()
        .hole(20)
        .pushPoints([(30, 20), (-30, 20), (30, -20), (-30, -20)])
        .hole(5)
    )
    
    # Export to multiple formats
    exporter = DollyExporter()
    formats_to_export = ['step', 'stl', 'svg', 'dxf', 'vrml']
    
    print(f"\nExporting to {len(formats_to_export)} formats...")
    exported_files = exporter.export_all_formats(
        demo_part, 
        'demo_part',
        formats_to_export
    )
    
    print("\n✅ Exported files:")
    for file in exported_files:
        size = os.path.getsize(file) / 1024  # KB
        print(f"  - {file} ({size:.1f} KB)")
    
    # Print viewing instructions
    print("\n📋 How to view each format:")
    print("  STEP: FreeCAD, Fusion 360, or online viewers")
    print("  STL:  Any 3D printing slicer, MeshLab, or online STL viewers")
    print("  SVG:  Any web browser, Inkscape, Illustrator")
    print("  DXF:  LibreCAD, AutoCAD, or online DXF viewers")
    print("  VRML: FreeWRL, Blender, or older 3D viewers")

# Create HTML viewer for SVG files
def create_svg_viewer():
    """Create an HTML page to view SVG exports"""
    html = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dolly Robot - SVG Technical Drawings</title>
    <style>
        body {
            font-family: -apple-system, BlinkMacSystemFont, sans-serif;
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
            background: #f5f5f5;
        }
        
        .header {
            background: #2563eb;
            color: white;
            padding: 30px;
            border-radius: 10px;
            text-align: center;
            margin-bottom: 30px;
        }
        
        h1 {
            margin: 0;
            font-size: 2.5em;
        }
        
        .drawing-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
            gap: 20px;
        }
        
        .drawing-card {
            background: white;
            border-radius: 8px;
            overflow: hidden;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        }
        
        .drawing-header {
            background: #f3f4f6;
            padding: 15px;
            border-bottom: 1px solid #e5e7eb;
        }
        
        .drawing-header h3 {
            margin: 0;
            color: #374151;
        }
        
        .drawing-content {
            padding: 20px;
            background: white;
            min-height: 300px;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        
        .svg-container {
            width: 100%;
            height: 300px;
            border: 1px solid #e5e7eb;
            border-radius: 4px;
            overflow: hidden;
        }
        
        .svg-container img,
        .svg-container object {
            width: 100%;
            height: 100%;
            object-fit: contain;
        }
        
        .info {
            background: #fef3c7;
            border: 1px solid #fbbf24;
            border-radius: 6px;
            padding: 15px;
            margin-bottom: 20px;
        }
        
        .viewer-options {
            background: white;
            padding: 20px;
            border-radius: 8px;
            margin-bottom: 20px;
        }
        
        .format-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 15px;
            margin-top: 15px;
        }
        
        .format-card {
            border: 1px solid #e5e7eb;
            border-radius: 6px;
            padding: 15px;
            text-align: center;
        }
        
        .format-card h4 {
            margin: 0 0 10px 0;
            color: #2563eb;
        }
        
        .format-card p {
            margin: 5px 0;
            font-size: 0.9em;
            color: #6b7280;
        }
    </style>
</head>
<body>
    <div class="header">
        <h1>🤖 Dolly Robot</h1>
        <p>Technical Drawings Viewer</p>
    </div>
    
    <div class="info">
        <h3>📋 About These Drawings</h3>
        <p>These SVG files are generated directly from CADQuery 3D models. They show accurate 2D projections of each part.</p>
        <p>SVG files can be opened in any web browser, edited in Inkscape/Illustrator, or used in documentation.</p>
    </div>
    
    <div class="viewer-options">
        <h2>Available Export Formats from CADQuery</h2>
        <div class="format-grid">
            <div class="format-card">
                <h4>STEP</h4>
                <p>CAD Exchange</p>
                <p>✓ Full 3D geometry</p>
                <p>✓ Editable in CAD</p>
            </div>
            <div class="format-card">
                <h4>STL</h4>
                <p>3D Printing</p>
                <p>✓ Direct to slicer</p>
                <p>✓ Mesh format</p>
            </div>
            <div class="format-card">
                <h4>SVG</h4>
                <p>2D Drawings</p>
                <p>✓ Browser viewable</p>
                <p>✓ Vector graphics</p>
            </div>
            <div class="format-card">
                <h4>DXF</h4>
                <p>Laser Cutting</p>
                <p>✓ 2D profiles</p>
                <p>✓ CAD compatible</p>
            </div>
            <div class="format-card">
                <h4>VRML</h4>
                <p>3D Visualization</p>
                <p>✓ Color support</p>
                <p>✓ Web viewable</p>
            </div>
            <div class="format-card">
                <h4>AMF</h4>
                <p>Advanced 3D Print</p>
                <p>✓ Color/material</p>
                <p>✓ Next-gen format</p>
            </div>
        </div>
    </div>
    
    <h2>SVG Drawing Gallery</h2>
    <div class="drawing-grid" id="drawingGrid">
        <!-- SVG files will be loaded here by JavaScript -->
    </div>
    
    <script>
        // In a real implementation, this would scan the SVG directory
        const svgFiles = [
            'dolly_frame_top.svg',
            'dolly_frame_front.svg', 
            'dolly_frame_side.svg',
            'dolly_base_plate_top.svg',
            'dolly_assembly_top.svg'
        ];
        
        const grid = document.getElementById('drawingGrid');
        
        svgFiles.forEach(file => {
            const card = document.createElement('div');
            card.className = 'drawing-card';
            
            const partName = file.replace('.svg', '').replace(/_/g, ' ');
            
            card.innerHTML = `
                <div class="drawing-header">
                    <h3>${partName}</h3>
                </div>
                <div class="drawing-content">
                    <div class="svg-container">
                        <object data="hardware/svg/${file}" type="image/svg+xml">
                            <img src="hardware/svg/${file}" alt="${partName}">
                        </object>
                    </div>
                </div>
            `;
            
            grid.appendChild(card);
        });
    </script>
</body>
</html>'''
    
    with open('docs/svg-viewer.html', 'w') as f:
        f.write(html)
    print("\nCreated: docs/svg-viewer.html")

if __name__ == "__main__":
    demo_multi_export()
    create_svg_viewer()
    
    print("\n💡 TIP: SVG files can be viewed directly in your browser!")
    print("   No special software needed for basic viewing.")

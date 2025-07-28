#!/usr/bin/env python3
"""
Dolly Robot - STEP File Viewer Helper
Helps users view the generated STEP files using various methods
"""

import os
import subprocess
import webbrowser
from pathlib import Path

class StepFileViewer:
    def __init__(self):
        self.step_dir = Path("hardware/step")
        self.viewers = {
            "freecad": {
                "name": "FreeCAD",
                "command": ["freecad"],
                "install": "brew install freecad  # or apt-get install freecad"
            },
            "autodesk": {
                "name": "Autodesk Viewer (Online)",
                "url": "https://viewer.autodesk.com/",
                "note": "Upload your STEP file"
            },
            "sharecad": {
                "name": "ShareCAD (Online)",
                "url": "https://www.sharecad.org/cadframe/load",
                "note": "Free, no registration"
            },
            "emachineshop": {
                "name": "eMachineShop (Online)",
                "url": "https://www.emachineshop.com/cad-viewer/",
                "note": "Good for technical details"
            },
            "3dviewer": {
                "name": "3DViewer.net",
                "url": "https://3dviewer.net/",
                "note": "Drag and drop files"
            }
        }
    
    def find_step_files(self):
        """Find all STEP files in the project"""
        step_files = []
        if self.step_dir.exists():
            for file in self.step_dir.rglob("*.step"):
                step_files.append(file)
            for file in self.step_dir.rglob("*.STEP"):
                step_files.append(file)
        return step_files
    
    def open_with_freecad(self, filepath):
        """Try to open file with FreeCAD"""
        try:
            subprocess.run(["freecad", str(filepath)])
            return True
        except FileNotFoundError:
            print("FreeCAD not found. Install with:")
            print("  macOS: brew install freecad")
            print("  Linux: sudo apt-get install freecad")
            print("  Windows: Download from freecadweb.org")
            return False
    
    def open_online_viewer(self, viewer_key):
        """Open online viewer in browser"""
        if viewer_key in self.viewers:
            viewer = self.viewers[viewer_key]
            print(f"\nOpening {viewer['name']}...")
            print(f"Note: {viewer.get('note', '')}")
            webbrowser.open(viewer['url'])
    
    def create_viewer_html(self):
        """Create an HTML page with all viewing options"""
        html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dolly Robot - STEP File Viewer Guide</title>
    <style>
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
            background: #f5f5f5;
            color: #333;
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
        
        .subtitle {
            margin-top: 10px;
            opacity: 0.9;
        }
        
        .section {
            background: white;
            padding: 25px;
            border-radius: 10px;
            margin-bottom: 20px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        }
        
        .viewer-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 20px;
            margin-top: 20px;
        }
        
        .viewer-card {
            border: 2px solid #e5e7eb;
            border-radius: 8px;
            padding: 20px;
            transition: all 0.3s ease;
        }
        
        .viewer-card:hover {
            border-color: #2563eb;
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(37,99,235,0.2);
        }
        
        .viewer-card h3 {
            color: #2563eb;
            margin-top: 0;
        }
        
        .viewer-type {
            display: inline-block;
            padding: 4px 12px;
            background: #e5e7eb;
            border-radius: 20px;
            font-size: 0.85em;
            margin-bottom: 10px;
        }
        
        .viewer-type.online {
            background: #dbeafe;
            color: #1e40af;
        }
        
        .viewer-type.desktop {
            background: #d1fae5;
            color: #065f46;
        }
        
        .btn {
            display: inline-block;
            padding: 10px 20px;
            background: #2563eb;
            color: white;
            text-decoration: none;
            border-radius: 6px;
            margin-top: 10px;
            transition: background 0.3s ease;
        }
        
        .btn:hover {
            background: #1d4ed8;
        }
        
        .file-list {
            background: #f9fafb;
            border: 1px solid #e5e7eb;
            border-radius: 6px;
            padding: 20px;
            margin-top: 20px;
        }
        
        .file-item {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 10px;
            border-bottom: 1px solid #e5e7eb;
        }
        
        .file-item:last-child {
            border-bottom: none;
        }
        
        .instructions {
            background: #fef3c7;
            border: 1px solid #fbbf24;
            border-radius: 6px;
            padding: 15px;
            margin-bottom: 20px;
        }
        
        .instructions h4 {
            margin-top: 0;
            color: #92400e;
        }
        
        code {
            background: #f3f4f6;
            padding: 2px 6px;
            border-radius: 3px;
            font-family: 'Consolas', 'Monaco', monospace;
        }
    </style>
</head>
<body>
    <div class="header">
        <h1>🤖 Dolly Robot</h1>
        <div class="subtitle">STEP File Viewer Guide</div>
    </div>
    
    <div class="section">
        <h2>📋 Quick Start</h2>
        <div class="instructions">
            <h4>⚠️ First, generate the STEP files!</h4>
            <p>Run these commands in the project directory:</p>
            <pre><code>cd hardware/cad
python dolly_assembly.py
python dolly_frame_structure.py
python dolly_heavy_parts.py</code></pre>
        </div>
        
        <h3>Choose Your Viewing Method:</h3>
        
        <div class="viewer-grid">
            <!-- Online Viewers -->
            <div class="viewer-card">
                <span class="viewer-type online">Online - Free</span>
                <h3>Autodesk Viewer</h3>
                <p>Professional viewer with measurement tools. No installation needed.</p>
                <a href="https://viewer.autodesk.com/" target="_blank" class="btn">Open Autodesk Viewer</a>
                <p style="margin-top: 10px; font-size: 0.9em; color: #666;">
                    ✓ Measurements<br>
                    ✓ Sectioning<br>
                    ✓ Exploded views
                </p>
            </div>
            
            <div class="viewer-card">
                <span class="viewer-type online">Online - Free</span>
                <h3>ShareCAD</h3>
                <p>Quick and simple viewer. No registration required.</p>
                <a href="https://www.sharecad.org/cadframe/load" target="_blank" class="btn">Open ShareCAD</a>
                <p style="margin-top: 10px; font-size: 0.9em; color: #666;">
                    ✓ No signup<br>
                    ✓ Basic viewing<br>
                    ✓ Share links
                </p>
            </div>
            
            <div class="viewer-card">
                <span class="viewer-type online">Online - Free</span>
                <h3>3DViewer.net</h3>
                <p>Modern interface with good navigation. Drag & drop files.</p>
                <a href="https://3dviewer.net/" target="_blank" class="btn">Open 3DViewer</a>
                <p style="margin-top: 10px; font-size: 0.9em; color: #666;">
                    ✓ Modern UI<br>
                    ✓ Good performance<br>
                    ✓ Multiple formats
                </p>
            </div>
            
            <!-- Desktop Viewers -->
            <div class="viewer-card">
                <span class="viewer-type desktop">Desktop - Free</span>
                <h3>FreeCAD</h3>
                <p>Full CAD software. Can edit and export to other formats.</p>
                <div style="background: #f3f4f6; padding: 10px; border-radius: 4px; margin-top: 10px;">
                    <code>brew install freecad</code><br>
                    <code>apt-get install freecad</code>
                </div>
                <a href="https://www.freecadweb.org/" target="_blank" class="btn">Download FreeCAD</a>
            </div>
            
            <div class="viewer-card">
                <span class="viewer-type desktop">Desktop - Free</span>
                <h3>OpenSCAD</h3>
                <p>Programmer's CAD tool. Good for parametric viewing.</p>
                <div style="background: #f3f4f6; padding: 10px; border-radius: 4px; margin-top: 10px;">
                    <code>brew install openscad</code>
                </div>
                <a href="https://openscad.org/" target="_blank" class="btn">Download OpenSCAD</a>
            </div>
            
            <div class="viewer-card">
                <span class="viewer-type desktop">Desktop - Free*</span>
                <h3>Fusion 360</h3>
                <p>Professional CAD. Free for personal use.</p>
                <a href="https://www.autodesk.com/products/fusion-360/personal" target="_blank" class="btn">Get Fusion 360</a>
                <p style="margin-top: 10px; font-size: 0.9em; color: #666;">
                    ✓ Professional tools<br>
                    ✓ Cloud storage<br>
                    ✓ Rendering
                </p>
            </div>
        </div>
    </div>
    
    <div class="section">
        <h2>📁 Expected STEP Files</h2>
        <p>After running the CADQuery scripts, you should have these files:</p>
        
        <div class="file-list">
            <div class="file-item">
                <strong>dolly_complete_assembly.step</strong>
                <span>Full robot assembly</span>
            </div>
            <div class="file-item">
                <strong>dolly_frame_only.step</strong>
                <span>Aluminum frame structure</span>
            </div>
            <div class="file-item">
                <strong>dolly_main_base_plate.step</strong>
                <span>Base mounting plate</span>
            </div>
            <div class="file-item">
                <strong>dolly_mac_mini_mount.step</strong>
                <span>Mac Mini mounting bracket</span>
            </div>
            <div class="file-item">
                <strong>dolly_power_station_bracket.step</strong>
                <span>Power station holder</span>
            </div>
            <div class="file-item">
                <strong>dolly_belly_door.step</strong>
                <span>USB access door</span>
            </div>
        </div>
    </div>
    
    <div class="section">
        <h2>💡 Viewing Tips</h2>
        <ul>
            <li><strong>For Quick Viewing:</strong> Use online viewers - just drag and drop</li>
            <li><strong>For Measurements:</strong> Autodesk Viewer or FreeCAD</li>
            <li><strong>For Editing:</strong> FreeCAD or Fusion 360</li>
            <li><strong>For 3D Printing:</strong> Import into your slicer (most support STEP)</li>
            <li><strong>For Documentation:</strong> Take screenshots from multiple angles</li>
        </ul>
    </div>
    
    <div class="section">
        <h2>🔄 Converting STEP Files</h2>
        <p>Need a different format?</p>
        <ul>
            <li><strong>To STL:</strong> Use FreeCAD or your slicer software</li>
            <li><strong>To PDF:</strong> FreeCAD can export technical drawings</li>
            <li><strong>To Images:</strong> Take screenshots in any viewer</li>
            <li><strong>To DXF:</strong> For laser cutting - use FreeCAD</li>
        </ul>
    </div>
</body>
</html>"""
        
        with open("docs/step-viewer-guide.html", "w") as f:
            f.write(html)
        print("Created: docs/step-viewer-guide.html")
    
    def interactive_menu(self):
        """Interactive menu for viewing files"""
        print("\n🤖 Dolly Robot - STEP File Viewer")
        print("=" * 50)
        
        step_files = self.find_step_files()
        
        if not step_files:
            print("❌ No STEP files found!")
            print("\nPlease generate them first:")
            print("  cd hardware/cad")
            print("  python dolly_assembly.py")
            print("  python dolly_frame_structure.py")
            print("  python dolly_heavy_parts.py")
            return
        
        print(f"\n✅ Found {len(step_files)} STEP files:")
        for i, file in enumerate(step_files, 1):
            print(f"  {i}. {file.name}")
        
        print("\n📋 Viewing Options:")
        print("  1. Open with FreeCAD (if installed)")
        print("  2. Autodesk Viewer (online)")
        print("  3. ShareCAD (online)")
        print("  4. 3DViewer.net (online)")
        print("  5. Create viewer guide HTML")
        print("  0. Exit")
        
        while True:
            choice = input("\nSelect option (0-5): ")
            
            if choice == "0":
                break
            elif choice == "1":
                file_num = input("Which file number? ")
                try:
                    file_idx = int(file_num) - 1
                    if 0 <= file_idx < len(step_files):
                        self.open_with_freecad(step_files[file_idx])
                except:
                    print("Invalid file number")
            elif choice == "2":
                self.open_online_viewer("autodesk")
            elif choice == "3":
                self.open_online_viewer("sharecad")
            elif choice == "4":
                self.open_online_viewer("3dviewer")
            elif choice == "5":
                self.create_viewer_html()
                print("Opening viewer guide...")
                webbrowser.open("file://" + os.path.abspath("docs/step-viewer-guide.html"))

if __name__ == "__main__":
    viewer = StepFileViewer()
    viewer.interactive_menu()

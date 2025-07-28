#!/usr/bin/env python3
"""
Dolly Robot - Tactile Design Features
Parts designed with touch-based assembly in mind.
Every part has clear orientation and alignment features.
"""

import cadquery as cq

class TactileDesignParts:
    """Parts with enhanced tactile feedback for assembly"""
    
    def create_tactile_base_plate(self):
        """Base plate with tactile orientation features"""
        plate = (
            cq.Workplane("XY")
            .rect(280, 230)
            .extrude(6)
        )
        
        # Front identifier - three raised dots
        for x in [-20, 0, 20]:
            dot = (
                cq.Workplane("XY")
                .center(x, 105)
                .circle(5)
                .extrude(2)
            )
            plate = plate.union(dot)
        
        # Back identifier - single raised line
        line = (
            cq.Workplane("XY")
            .center(0, -105)
            .rect(60, 5)
            .extrude(2)
        )
        plate = plate.union(line)
        
        # Motor mounting slots with different widths
        # Left motor - wider slot (10mm)
        plate = (
            plate.faces(">Z")
            .workplane()
            .center(-100, 0)
            .slot2D(40, 10, 90)
            .cutThruAll()
        )
        
        # Right motor - narrower slot (8mm)
        plate = (
            plate.faces(">Z")
            .workplane()
            .center(100, 0)
            .slot2D(40, 8, 90)
            .cutThruAll()
        )
        
        # Corner mounting holes with tactile rings
        corners = [(130, 95), (-130, 95), (130, -95), (-130, -95)]
        for i, (x, y) in enumerate(corners):
            # Different pattern for each corner
            rings = i + 1  # 1-4 rings
            for r in range(rings):
                ring = (
                    cq.Workplane("XY")
                    .center(x, y)
                    .circle(10 + r * 3)
                    .circle(8 + r * 3)
                    .extrude(1)
                )
                plate = plate.union(ring)
            
            # Central hole
            plate = (
                plate.faces(">Z")
                .workplane()
                .center(x, y)
                .hole(5.2)
            )
        
        # Raised edge for cable management
        edge_height = 10
        edge = (
            cq.Workplane("XY")
            .rect(260, 210)
            .extrude(edge_height)
            .faces(">Z")
            .rect(240, 190)
            .cutThruAll()
        )
        plate = plate.union(edge.translate((0, 0, 6)))
        
        return plate
    
    def create_orientation_key(self):
        """Universal orientation key for all assemblies"""
        key = (
            cq.Workplane("XY")
            .moveTo(0, 0)
            # Arrow shape pointing forward
            .lineTo(-10, -10)
            .lineTo(-5, -10)
            .lineTo(-5, -20)
            .lineTo(5, -20)
            .lineTo(5, -10)
            .lineTo(10, -10)
            .close()
            .extrude(3)
        )
        
        # Add braille-like dots for "F" (front)
        # Pattern: ⠋ (dots 1,2,4)
        dots = [(0, 5), (-3, 2), (-3, -1)]
        for x, y in dots:
            dot = (
                cq.Workplane("XY")
                .center(x, y)
                .circle(1.5)
                .extrude(1.5)
            )
            key = key.union(dot)
        
        return key
    
    def create_cable_guide_with_texture(self):
        """Cable guide with textured paths"""
        guide = (
            cq.Workplane("XY")
            .rect(80, 60)
            .extrude(15)
        )
        
        # Different channel textures for different cable types
        # Smooth channel for power (left)
        guide = (
            guide.faces(">Z")
            .workplane()
            .center(-20, 0)
            .slot2D(10, 50, 90)
            .cutBlind(-10)
        )
        
        # Ribbed channel for data (center)
        for i in range(5):
            rib = (
                cq.Workplane("XY")
                .center(0, -20 + i * 10)
                .rect(8, 2)
                .extrude(12)
            )
            guide = guide.cut(rib)
        
        # Dotted channel for sensor wires (right)
        for i in range(10):
            dot = (
                cq.Workplane("XY")
                .center(20, -25 + i * 5)
                .circle(2)
                .extrude(10)
            )
            guide = guide.cut(dot)
        
        # Entry guides with flared openings
        for x in [-20, 0, 20]:
            flare = (
                cq.Workplane("XZ")
                .center(x, -7.5)
                .circle(8)
                .workplane(offset=5)
                .circle(5)
                .loft()
                .translate((0, -30, 0))
            )
            guide = guide.union(flare)
        
        return guide
    
    def create_snap_fit_with_feedback(self):
        """Snap-fit joint with tactile and audible feedback"""
        # Male part
        male = (
            cq.Workplane("XY")
            .rect(30, 40)
            .extrude(20)
        )
        
        # Snap tab with specific profile
        tab = (
            cq.Workplane("YZ")
            .moveTo(0, 0)
            .lineTo(0, 10)
            .lineTo(2, 12)  # Lead-in angle
            .lineTo(2, 15)
            .lineTo(-1, 18)  # Snap ridge
            .lineTo(-1, 20)
            .close()
            .extrude(20)
            .translate((15, 0, 0))
        )
        male = male.union(tab)
        
        # Alignment ridges
        for y in [-15, 0, 15]:
            ridge = (
                cq.Workplane("XY")
                .center(0, y)
                .rect(30, 2)
                .extrude(1)
                .translate((0, 0, 20))
            )
            male = male.union(ridge)
        
        # Female part
        female = (
            cq.Workplane("XY")
            .rect(34, 44)
            .extrude(22)
            .faces(">Z")
            .rect(30, 40)
            .cutBlind(-20)
        )
        
        # Snap receiver with click ridge
        receiver = (
            cq.Workplane("XY")
            .center(15, 0)
            .rect(4, 20)
            .extrude(22)
        )
        female = female.cut(receiver)
        
        # Click ridge for audible feedback
        click_ridge = (
            cq.Workplane("XZ")
            .center(13, -18)
            .rect(2, 2)
            .extrude(20)
        )
        female = female.union(click_ridge)
        
        # Alignment grooves matching male ridges
        for y in [-15, 0, 15]:
            groove = (
                cq.Workplane("XY")
                .center(0, y)
                .rect(30, 2.2)
                .extrude(1.2)
                .translate((0, 0, 21.8))
            )
            female = female.cut(groove)
        
        return male, female
    
    def create_modular_connector_system(self):
        """Universal connector with fool-proof orientation"""
        # Base connector body
        connector = (
            cq.Workplane("XY")
            .polygon([
                (0, 20),      # Top point (narrow)
                (15, 10),     # Right upper
                (15, -10),    # Right lower  
                (0, -15),     # Bottom (wide)
                (-15, -10),   # Left lower
                (-15, 10)     # Left upper
            ])
            .extrude(25)
        )
        
        # Pin holes with different sizes
        # Power pins (large)
        for x in [-8, 8]:
            connector = (
                connector.faces(">Z")
                .workplane()
                .center(x, -5)
                .hole(4)
            )
        
        # Data pins (medium)
        for x in [-5, 0, 5]:
            connector = (
                connector.faces(">Z")
                .workplane()
                .center(x, 5)
                .hole(2.5)
            )
        
        # Orientation pin (small, offset)
        connector = (
            connector.faces(">Z")
            .workplane()
            .center(-10, 10)
            .hole(1.5)
        )
        
        # Tactile identification grooves
        # Left side - power (vertical lines)
        for i in range(3):
            groove = (
                cq.Workplane("XZ")
                .center(-15, -12.5 + i * 5)
                .rect(2, 20)
                .extrude(3)
            )
            connector = connector.cut(groove)
        
        # Right side - data (horizontal lines)  
        for i in range(5):
            groove = (
                cq.Workplane("YZ")
                .center(15, -12.5 + i * 5)
                .rect(2, 10)
                .extrude(3)
            )
            connector = connector.cut(groove)
        
        # Locking tab slot
        connector = (
            connector.faces(">Y")
            .workplane()
            .center(0, -12.5)
            .rect(10, 5)
            .cutBlind(-5)
        )
        
        return connector
    
    def create_button_array_with_shapes(self):
        """Control panel with different button shapes"""
        panel = (
            cq.Workplane("XY")
            .rect(120, 80)
            .extrude(3)
        )
        
        # Different button holes with raised edges
        # Circle - Power (most important)
        panel = (
            panel.faces(">Z")
            .workplane()
            .center(-40, 20)
            .circle(12)
            .extrude(2)
            .faces(">Z")
            .circle(10)
            .cutThruAll()
        )
        
        # Square - Stop
        panel = (
            panel.faces(">Z")
            .workplane()
            .center(0, 20)
            .rect(20, 20)
            .extrude(2)
            .faces(">Z")
            .rect(16, 16)
            .cutThruAll()
        )
        
        # Triangle - Start  
        triangle = (
            cq.Workplane("XY")
            .center(40, 20)
            .polygon(3, 12)
            .extrude(5)
            .faces(">Z")
            .polygon(3, 10)
            .cutThruAll()
        )
        panel = panel.union(triangle)
        
        # Directional pad (cross shape)
        cross_center = (0, -20)
        cross = (
            cq.Workplane("XY")
            .center(*cross_center)
            .rect(30, 10)
            .extrude(2)
        )
        cross = cross.union(
            cq.Workplane("XY")
            .center(*cross_center)
            .rect(10, 30)
            .extrude(2)
        )
        panel = panel.union(cross)
        
        # Cut button holes in cross
        for x, y in [(0, -10), (0, -30), (-10, -20), (10, -20)]:
            panel = (
                panel.faces(">Z")
                .workplane()
                .center(x, y)
                .circle(3)
                .cutThruAll()
            )
        
        # Add braille labels (simplified)
        # P for power
        for x, y in [(-47, 5), (-44, 5), (-47, 2), (-44, 2)]:
            dot = (
                cq.Workplane("XY")
                .center(x, y)
                .circle(0.75)
                .extrude(0.5)
                .translate((0, 0, 3))
            )
            panel = panel.union(dot)
        
        return panel

# Generate tactile design examples
if __name__ == "__main__":
    print("Generating tactile design parts...")
    print("These parts emphasize touch-based assembly")
    print("=" * 50)
    
    tactile = TactileDesignParts()
    
    parts = [
        ("tactile_base_plate", tactile.create_tactile_base_plate()),
        ("orientation_key", tactile.create_orientation_key()),
        ("cable_guide_textured", tactile.create_cable_guide_with_texture()),
        ("button_panel_shapes", tactile.create_button_array_with_shapes()),
        ("modular_connector", tactile.create_modular_connector_system())
    ]
    
    # Snap-fit returns two parts
    male, female = tactile.create_snap_fit_with_feedback()
    parts.append(("snap_fit_male", male))
    parts.append(("snap_fit_female", female))
    
    for name, part in parts:
        cq.exporters.export(part, f"tactile_parts/dolly_{name}.step")
        cq.exporters.export(part, f"tactile_parts/dolly_{name}.stl")
        print(f"  ✓ {name}")
    
    print("\n" + "=" * 50)
    print("Tactile Design Features:")
    print("  • Asymmetric shapes prevent backward assembly")
    print("  • Different textures identify cable types")  
    print("  • Raised dots/lines indicate orientation")
    print("  • Snap-fits provide audible feedback")
    print("  • Button shapes indicate function")
    print("  • Braille labels where helpful")
    print("\nThese features make assembly possible without sight!")
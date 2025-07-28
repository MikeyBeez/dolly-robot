#!/usr/bin/env python3
"""
Dolly Robot - Frame Structure Only
This file shows just the aluminum extrusion frame structure.
This is the skeleton that everything else mounts to.
"""

import cadquery as cq

class DollyFrameStructure:
    """Dolly robot aluminum extrusion frame"""
    
    def __init__(self):
        # Frame dimensions
        self.height = 600  # ~24 inches tall
        self.width = 300   # Base width
        self.depth = 250   # Base depth
        
        # Extrusion profile (2020 aluminum)
        self.extrusion_size = 20
        
        # Heights for different sections
        self.base_height = 40
        self.power_bay_height = 200
        self.mac_mini_height = 300
        self.shoulder_height = 420
        self.top_height = 480
        
    def create_extrusion_profile(self):
        """Create 2020 aluminum extrusion profile"""
        size = self.extrusion_size
        slot_width = 6
        slot_depth = 8
        
        # Main square
        profile = cq.Workplane("XY").box(size, size, size)
        
        # Cut T-slots on all 4 sides
        for angle in [0, 90, 180, 270]:
            slot = (
                cq.Workplane("XY")
                .center(0, size/2)
                .rect(slot_width, slot_depth * 2)
                .extrude(size)
                .rotate((0, 0, 0), (0, 0, 1), angle)
            )
            profile = profile.cut(slot)
            
        return profile
    
    def create_frame(self):
        """Create the complete frame structure"""
        frame_parts = []
        
        # BASE RECTANGLE
        # Front and back horizontals
        for y in [self.depth/2 - 10, -self.depth/2 + 10]:
            beam = (
                cq.Workplane("XY")
                .box(self.width - 20, self.extrusion_size, self.extrusion_size)
                .translate((0, y, self.base_height))
            )
            frame_parts.append(beam)
        
        # Left and right horizontals
        for x in [self.width/2 - 10, -self.width/2 + 10]:
            beam = (
                cq.Workplane("XY")
                .box(self.extrusion_size, self.depth - 20, self.extrusion_size)
                .translate((x, 0, self.base_height))
            )
            frame_parts.append(beam)
        
        # VERTICAL POSTS (4 corners)
        post_positions = [
            (self.width/2 - 10, self.depth/2 - 10),
            (-self.width/2 + 10, self.depth/2 - 10),
            (self.width/2 - 10, -self.depth/2 + 10),
            (-self.width/2 + 10, -self.depth/2 + 10)
        ]
        
        for x, y in post_positions:
            post = (
                cq.Workplane("XY")
                .box(self.extrusion_size, self.extrusion_size, 
                     self.top_height - self.base_height)
                .translate((x, y, (self.top_height + self.base_height)/2))
            )
            frame_parts.append(post)
        
        # HORIZONTAL SUPPORTS AT KEY HEIGHTS
        support_heights = [
            self.power_bay_height,    # Power station level
            self.mac_mini_height,     # Mac Mini level
            self.shoulder_height,     # Arm mounting level
            self.top_height          # Top level
        ]
        
        for height in support_heights:
            # Front and back
            for y in [self.depth/2 - 10, -self.depth/2 + 10]:
                beam = (
                    cq.Workplane("XY")
                    .box(self.width - 20, self.extrusion_size, self.extrusion_size)
                    .translate((0, y, height))
                )
                frame_parts.append(beam)
            
            # Sides (only at some levels for arm clearance)
            if height in [self.power_bay_height, self.top_height]:
                for x in [self.width/2 - 10, -self.width/2 + 10]:
                    beam = (
                        cq.Workplane("XY")
                        .box(self.extrusion_size, self.depth - 20, self.extrusion_size)
                        .translate((x, 0, height))
                    )
                    frame_parts.append(beam)
        
        # DIAGONAL BRACES (back only for rigidity)
        # Lower brace
        brace_length = ((self.width - 40)**2 + (self.power_bay_height - self.base_height)**2)**0.5
        lower_brace = (
            cq.Workplane("XZ")
            .rect(self.extrusion_size, brace_length)
            .extrude(self.extrusion_size)
            .rotate((0, 0, 0), (0, 1, 0), 45)
            .translate((0, self.depth/2 - 10, (self.power_bay_height + self.base_height)/2))
        )
        frame_parts.append(lower_brace)
        
        # Combine all parts
        frame = frame_parts[0]
        for part in frame_parts[1:]:
            frame = frame.union(part)
            
        return frame
    
    def create_mounting_plates(self):
        """Create key mounting plates that attach to frame"""
        plates = []
        
        # Base plate for motors/wheels
        base_plate = (
            cq.Workplane("XY")
            .box(self.width - 40, self.depth - 40, 5)
            .translate((0, 0, self.base_height + self.extrusion_size/2 + 2.5))
            .edges("|Z").fillet(5)
        )
        plates.append(base_plate)
        
        # Mac Mini mounting plate
        mac_plate = (
            cq.Workplane("XY")
            .box(220, 220, 3)
            .translate((0, 0, self.mac_mini_height + self.extrusion_size/2 + 1.5))
            .edges("|Z").fillet(5)
        )
        plates.append(mac_plate)
        
        # Power station support plate
        power_plate = (
            cq.Workplane("XY")
            .box(200, 150, 3)
            .translate((0, 0, self.power_bay_height + self.extrusion_size/2 + 1.5))
            .edges("|Z").fillet(5)
        )
        plates.append(power_plate)
        
        # Combine plates
        all_plates = plates[0]
        for plate in plates[1:]:
            all_plates = all_plates.union(plate)
            
        return all_plates

# Generate frame files
if __name__ == "__main__":
    print("Generating Dolly robot frame structure...")
    
    # Create frame only
    frame_structure = DollyFrameStructure()
    frame = frame_structure.create_frame()
    
    # Export frame
    cq.exporters.export(frame, "dolly_frame_only.step")
    cq.exporters.export(frame, "dolly_frame_only.stl")
    
    # Create frame with mounting plates
    frame_with_plates = frame.union(frame_structure.create_mounting_plates())
    cq.exporters.export(frame_with_plates, "dolly_frame_with_plates.step")
    cq.exporters.export(frame_with_plates, "dolly_frame_with_plates.stl")
    
    print("\nFrame files created:")
    print("  - dolly_frame_only.step (just extrusion)")
    print("  - dolly_frame_only.stl")
    print("  - dolly_frame_with_plates.step (with mounting surfaces)")
    print("  - dolly_frame_with_plates.stl")
    print("\nUse 2020 aluminum extrusion to build this frame.")
    print("See dolly_assembly.py for complete robot visualization.")
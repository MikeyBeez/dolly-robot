#!/usr/bin/env python3
"""
Dolly Robot - Complete Assembly
This file shows the entire robot assembled together.
Individual components are simplified - see component files for details.
"""

import cadquery as cq

class DollyRobotAssembly:
    """Complete Dolly robot assembly"""
    
    def __init__(self):
        # Overall dimensions
        self.total_height = 610  # 24 inches
        self.base_width = 300
        self.base_depth = 250
        
        # Component positions (from bottom)
        self.wheel_height = 35
        self.base_plate_height = 40
        self.power_station_bottom = 80
        self.mac_mini_bottom = 250
        self.torso_top = 400
        self.shoulder_height = 420
        self.head_bottom = 480
        
    def create_simplified_base(self):
        """Simplified base with wheels"""
        # Base plate
        base = (
            cq.Workplane("XY")
            .box(self.base_width, self.base_depth, 5)
            .translate((0, 0, self.base_plate_height))
        )
        
        # Drive wheels (simplified as cylinders)
        wheel_diameter = 70
        wheel_width = 25
        wheel_spacing = 200
        
        for x in [-wheel_spacing/2, wheel_spacing/2]:
            wheel = (
                cq.Workplane("YZ")
                .circle(wheel_diameter/2)
                .extrude(wheel_width)
                .translate((x, 0, self.wheel_height))
            )
            base = base.union(wheel)
        
        # Casters (simplified)
        caster_positions = [(80, 80), (-80, 80), (80, -80), (-80, -80)]
        for x, y in caster_positions:
            caster = (
                cq.Workplane("XY")
                .circle(15)
                .extrude(30)
                .translate((x, y, 10))
            )
            base = base.union(caster)
            
        return base
    
    def create_frame_structure(self):
        """Aluminum extrusion frame (simplified)"""
        extrusion_size = 20
        
        # Vertical posts
        posts = []
        post_positions = [
            (self.base_width/2 - 30, self.base_depth/2 - 30),
            (-self.base_width/2 + 30, self.base_depth/2 - 30),
            (self.base_width/2 - 30, -self.base_depth/2 + 30),
            (-self.base_width/2 + 30, -self.base_depth/2 + 30)
        ]
        
        frame = None
        for x, y in post_positions:
            post = (
                cq.Workplane("XY")
                .box(extrusion_size, extrusion_size, self.torso_top)
                .translate((x, y, self.torso_top/2 + self.base_plate_height))
            )
            frame = post if frame is None else frame.union(post)
            
        return frame
    
    def create_torso_components(self):
        """Simplified torso with Mac Mini and power station"""
        torso = cq.Workplane("XY")
        
        # Power station (simplified box)
        power_station = (
            cq.Workplane("XY")
            .box(180, 120, 130)
            .translate((0, 0, self.power_station_bottom + 65))
            .edges("|Z").fillet(10)
        )
        torso = torso.union(power_station)
        
        # Mac Mini (simplified box)
        mac_mini = (
            cq.Workplane("XY")
            .box(197, 197, 36)
            .translate((0, 0, self.mac_mini_bottom + 18))
            .edges("|Z").fillet(5)
        )
        torso = torso.union(mac_mini)
        
        # Belly door location (simplified)
        door_indicator = (
            cq.Workplane("XZ")
            .rect(120, 80)
            .extrude(3)
            .translate((0, -self.base_depth/2, 
                       (self.power_station_bottom + self.mac_mini_bottom)/2))
        )
        torso = torso.union(door_indicator)
        
        return torso
    
    def create_arms(self):
        """Simplified robot arms"""
        # Shoulder joint
        shoulder_width = 60
        shoulder_offset = 100
        
        arms = None
        for side in [-1, 1]:  # Left and right arms
            # Upper arm
            upper_arm = (
                cq.Workplane("XY")
                .box(30, 30, 150)
                .translate((side * shoulder_offset, 0, 
                           self.shoulder_height - 75))
                .rotate((0, 0, 0), (1, 0, 0), side * 30)
            )
            
            # Lower arm  
            lower_arm = (
                cq.Workplane("XY")
                .box(25, 25, 120)
                .translate((side * (shoulder_offset + 40), 0,
                           self.shoulder_height - 180))
                .rotate((0, 0, 0), (1, 0, 0), side * 45)
            )
            
            # Gripper (simplified)
            gripper = (
                cq.Workplane("XY")
                .box(40, 15, 60)
                .translate((side * (shoulder_offset + 60), 0,
                           self.shoulder_height - 280))
            )
            
            arm_assembly = upper_arm.union(lower_arm).union(gripper)
            arms = arm_assembly if arms is None else arms.union(arm_assembly)
            
        return arms
    
    def create_head(self):
        """Simplified head with camera indicators"""
        # Head base
        head = (
            cq.Workplane("XY")
            .box(120, 100, 80)
            .translate((0, 0, self.head_bottom + 40))
            .edges("|Z").fillet(15)
        )
        
        # Camera indicators (simplified as cylinders)
        # Main camera
        camera1 = (
            cq.Workplane("XZ")
            .circle(20)
            .extrude(10)
            .translate((0, -50, self.head_bottom + 60))
        )
        head = head.union(camera1)
        
        # Detail camera
        camera2 = (
            cq.Workplane("XZ")
            .circle(15)
            .extrude(8)
            .translate((0, -50, self.head_bottom + 30))
        )
        head = head.union(camera2)
        
        # Status display area
        display = (
            cq.Workplane("XZ")
            .rect(80, 40)
            .extrude(2)
            .translate((0, -50, self.head_bottom + 40))
        )
        head = head.cut(display)
        
        return head
    
    def assemble_robot(self):
        """Combine all components into complete robot"""
        # Start with base
        robot = self.create_simplified_base()
        
        # Add frame
        frame = self.create_frame_structure()
        robot = robot.union(frame)
        
        # Add torso components
        torso = self.create_torso_components()
        robot = robot.union(torso)
        
        # Add arms
        arms = self.create_arms()
        robot = robot.union(arms)
        
        # Add head
        head = self.create_head()
        robot = robot.union(head)
        
        return robot

# Generate the complete assembly
if __name__ == "__main__":
    print("Generating Dolly robot complete assembly...")
    
    dolly = DollyRobotAssembly()
    complete_robot = dolly.assemble_robot()
    
    # Export the complete assembly
    cq.exporters.export(complete_robot, "dolly_complete_assembly.step")
    cq.exporters.export(complete_robot, "dolly_complete_assembly.stl")
    
    print("Assembly files created:")
    print("  - dolly_complete_assembly.step")
    print("  - dolly_complete_assembly.stl")
    print("\nThis is a simplified representation.")
    print("See individual component files in hardware/cad/ for detailed parts.")
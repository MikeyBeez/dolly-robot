#!/usr/bin/env python3
"""
Dolly Robot - Base Frame CAD Design
Parametric design for the 2-foot circuit builder configuration
"""

import cadquery as cq

class DollyFrame:
    """Dolly robot base frame generator"""
    
    def __init__(self):
        # Frame dimensions (24" tall robot)
        self.total_height = 610  # ~24 inches in mm
        self.frame_width = 300   # Base width
        self.frame_depth = 250   # Base depth
        
        # Component spaces
        self.mac_mini_width = 197
        self.mac_mini_depth = 197
        self.mac_mini_height = 36
        
        # Power station approximate size (EcoFlow River)
        self.power_width = 180
        self.power_depth = 120
        self.power_height = 130
        
        # Extrusion size (2020 aluminum)
        self.extrusion_size = 20
        
    def create_base_plate(self):
        """Create the base mounting plate"""
        base = (
            cq.Workplane("XY")
            .rect(self.frame_width, self.frame_depth)
            .extrude(5)  # 5mm thick aluminum or printed plate
        )
        
        # Mounting holes for extrusion
        base = (
            base.faces(">Z")
            .workplane()
            .rect(
                self.frame_width - self.extrusion_size * 2,
                self.frame_depth - self.extrusion_size * 2,
                forConstruction=True
            )
            .vertices()
            .hole(5.2)  # M5 bolts for extrusion
        )
        
        # Caster wheel mounting points
        caster_offset = 80
        base = (
            base.faces(">Z")
            .workplane()
            .pushPoints([
                (caster_offset, caster_offset),
                (-caster_offset, caster_offset),
                (caster_offset, -caster_offset),
                (-caster_offset, -caster_offset)
            ])
            .hole(6.5)  # Caster mounting bolts
        )
        
        return base
    
    def create_mac_mini_mount(self):
        """Create mounting bracket for Mac Mini"""
        # Base plate
        mount = (
            cq.Workplane("XY")
            .rect(self.mac_mini_width + 20, self.mac_mini_depth + 20)
            .extrude(3)
        )
        
        # Side walls for Mini
        mount = (
            mount.faces(">Z")
            .workplane()
            .rect(self.mac_mini_width + 4, self.mac_mini_depth + 4)
            .extrude(20)
            .faces(">Z")
            .workplane()
            .rect(self.mac_mini_width, self.mac_mini_depth)
            .cutThruAll()
        )
        
        # Ventilation slots
        for i in range(5):
            mount = (
                mount.faces(">Y")
                .workplane(offset=-10 - i*8)
                .rect(150, 4)
                .cutThruAll()
            )
        
        # Cable management hole
        mount = (
            mount.faces("<Z")
            .workplane()
            .center(0, -self.mac_mini_depth/2 + 30)
            .rect(60, 20)
            .cutThruAll()
        )
        
        return mount
    
    def create_power_station_bay(self):
        """Create mounting bay for portable power station"""
        bay = (
            cq.Workplane("XY")
            .rect(self.power_width + 10, self.power_depth + 10)
            .extrude(3)
        )
        
        # Side rails to hold power station
        rail_height = 50
        bay = (
            bay.faces(">Z")
            .workplane()
            .rect(self.power_width + 10, self.power_depth + 10, forConstruction=True)
            .vertices()
            .rect(20, 20)
            .extrude(rail_height)
        )
        
        # Strap slots for securing
        bay = (
            bay.faces(">X")
            .workplane(offset=-rail_height/2)
            .rect(10, 15)
            .cutThruAll()
        )
        
        return bay
    
    def create_belly_door(self):
        """Create the USB cable access door"""
        door_width = 120
        door_height = 80
        
        # Door panel
        door = (
            cq.Workplane("XY")
            .rect(door_width, door_height)
            .extrude(3)
        )
        
        # Round the corners
        door = door.edges("|Z").fillet(10)
        
        # Hinge pin holes
        door = (
            door.faces(">Y")
            .workplane()
            .center(-door_width/2 + 5, 0)
            .hole(3)  # 3mm pin
            .center(door_width - 10, 0)
            .hole(3)
        )
        
        # Handle indent
        door = (
            door.faces(">Z")
            .workplane()
            .center(0, -door_height/2 + 15)
            .rect(40, 8)
            .cutBlind(-1.5)
        )
        
        return door
    
    def create_cable_reel(self):
        """Create retractable USB cable reel"""
        reel_diameter = 80
        reel_width = 30
        
        # Main reel body
        reel = (
            cq.Workplane("XY")
            .circle(reel_diameter/2)
            .extrude(reel_width)
        )
        
        # Cable channel
        reel = (
            reel.faces(">Z")
            .workplane()
            .circle(reel_diameter/2 - 5)
            .circle(reel_diameter/2 - 15)
            .cutThruAll()
        )
        
        # Center shaft hole
        reel = (
            reel.faces(">Z")
            .workplane()
            .circle(4)  # 8mm shaft
            .cutThruAll()
        )
        
        # Cable anchor point
        reel = (
            reel.faces(">Z")
            .workplane()
            .center(reel_diameter/2 - 10, 0)
            .rect(8, 4)
            .cutBlind(-10)
        )
        
        return reel

# Generate all parts
if __name__ == "__main__":
    dolly = DollyFrame()
    
    # Export parts
    base_plate = dolly.create_base_plate()
    cq.exporters.export(base_plate, "dolly_base_plate.step")
    
    mac_mount = dolly.create_mac_mini_mount()
    cq.exporters.export(mac_mount, "dolly_mac_mini_mount.step")
    
    power_bay = dolly.create_power_station_bay()
    cq.exporters.export(power_bay, "dolly_power_bay.step")
    
    belly_door = dolly.create_belly_door()
    cq.exporters.export(belly_door, "dolly_belly_door.step")
    
    cable_reel = dolly.create_cable_reel()
    cq.exporters.export(cable_reel, "dolly_cable_reel.step")
    
    print("Dolly frame components generated successfully!")
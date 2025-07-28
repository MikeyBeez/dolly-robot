#!/usr/bin/env python3
"""
Dolly Robot - Heavy Duty Parts
These are the structural parts that need to be strong.
Can be made from aluminum plate, steel, or thick PETG/ABS.
"""

import cadquery as cq

class DollyHeavyParts:
    """Heavy duty structural components"""
    
    def __init__(self):
        self.material_thickness = 6  # 6mm aluminum or 8mm printed
        
    def create_main_base_plate(self):
        """Main structural base that everything mounts to"""
        plate = (
            cq.Workplane("XY")
            .rect(280, 230)  # Fits inside frame
            .extrude(self.material_thickness)
        )
        
        # Large center cutout for weight reduction
        plate = (
            plate.faces(">Z")
            .rect(180, 130)
            .cutThruAll()
        )
        
        # Motor mounting slots (adjustable)
        motor_spacing = 200
        slot_length = 40
        slot_width = 8
        
        for x in [-motor_spacing/2, motor_spacing/2]:
            plate = (
                plate.faces(">Z")
                .workplane()
                .center(x, 0)
                .slot2D(slot_length, slot_width, 90)
                .cutThruAll()
            )
        
        # Frame mounting holes (M5)
        mount_pattern = [
            (130, 105), (-130, 105), 
            (130, -105), (-130, -105)
        ]
        
        for x, y in mount_pattern:
            plate = (
                plate.faces(">Z")
                .workplane()
                .center(x, y)
                .hole(5.2)
            )
        
        # Caster mounting (M6)
        caster_pattern = [(80, 80), (-80, 80), (80, -80), (-80, -80)]
        for x, y in caster_pattern:
            plate = (
                plate.faces(">Z")
                .workplane()
                .center(x, y)
                .hole(6.2)
            )
            
        # Round corners
        plate = plate.edges("|Z").fillet(10)
        
        return plate
    
    def create_motor_mount_plate(self):
        """Heavy duty NEMA 17 motor mount"""
        # Base plate
        mount = (
            cq.Workplane("XY")
            .rect(60, 60)
            .extrude(self.material_thickness)
        )
        
        # NEMA 17 mounting pattern
        nema17_spacing = 31
        mount = (
            mount.faces(">Z")
            .rect(nema17_spacing, nema17_spacing, forConstruction=True)
            .vertices()
            .hole(3.2)  # M3 bolts
        )
        
        # Center hole for motor shaft
        mount = (
            mount.faces(">Z")
            .hole(23)  # 22mm + clearance
        )
        
        # Slots for frame mounting
        mount = (
            mount.faces(">Z")
            .workplane()
            .center(0, 25)
            .slot2D(30, 5.5, 0)
            .cutThruAll()
            .center(0, -50)
            .slot2D(30, 5.5, 0)
            .cutThruAll()
        )
        
        return mount
    
    def create_mac_mini_security_plate(self):
        """Plate to secure Mac Mini with anti-vibration"""
        width = 210
        depth = 210
        
        plate = (
            cq.Workplane("XY")
            .rect(width, depth)
            .extrude(self.material_thickness/2)  # Thinner is OK here
        )
        
        # Mac Mini outline (slightly larger)
        plate = (
            plate.faces(">Z")
            .rect(199, 199)
            .extrude(2)  # Small lip
        )
        
        # Vibration damper mounting holes
        damper_pattern = [
            (90, 90), (-90, 90),
            (90, -90), (-90, -90)
        ]
        
        for x, y in damper_pattern:
            # Hole for rubber damper
            plate = (
                plate.faces(">Z")
                .workplane()
                .center(x, y)
                .hole(8)  # For rubber inserts
            )
        
        # Cable management slots
        plate = (
            plate.faces(">Z")
            .workplane()
            .center(0, -95)
            .slot2D(60, 20, 0)
            .cutThruAll()
        )
        
        # Ventilation pattern
        vent_spacing = 15
        for i in range(-3, 4):
            for j in range(-3, 4):
                if abs(i) + abs(j) <= 4:  # Diamond pattern
                    plate = (
                        plate.faces(">Z")
                        .workplane()
                        .center(i * vent_spacing, j * vent_spacing)
                        .hole(8)
                    )
        
        return plate
    
    def create_power_station_bracket(self):
        """Universal bracket for different power stations"""
        # L-shaped bracket
        bracket = (
            cq.Workplane("XY")
            .rect(200, 40)
            .extrude(self.material_thickness)
        )
        
        # Vertical portion
        vertical = (
            cq.Workplane("XZ")
            .rect(self.material_thickness, 80)
            .extrude(200)
            .translate((0, -20 + self.material_thickness/2, 40))
        )
        
        bracket = bracket.union(vertical)
        
        # Mounting slots (universal)
        for x in [-80, -40, 0, 40, 80]:
            bracket = (
                bracket.faces(">Y")
                .workplane()
                .center(x, -20)
                .slot2D(15, 6, 90)
                .cutThruAll()
            )
        
        # Strap slots
        bracket = (
            bracket.faces(">Z")
            .workplane()
            .center(-90, 0)
            .slot2D(15, 30, 90)
            .cutThruAll()
            .center(180, 0)
            .slot2D(15, 30, 90)
            .cutThruAll()
        )
        
        # Reinforce corners
        bracket = bracket.edges("|Y").fillet(3)
        
        return bracket
    
    def create_arm_base_joint(self):
        """Heavy duty shoulder joint for arms"""
        # Main cylinder
        base_diameter = 80
        base_height = 40
        
        joint = (
            cq.Workplane("XY")
            .circle(base_diameter/2)
            .extrude(base_height)
        )
        
        # Bearing seat (608 bearing)
        joint = (
            joint.faces(">Z")
            .hole(22)  # 608 bearing OD
            .faces(">Z")
            .workplane(offset=-7)
            .hole(22, 10)  # Bearing depth
        )
        
        # Shaft hole
        joint = (
            joint.faces(">Z")
            .hole(8)  # 8mm shaft
        )
        
        # Mounting flange
        flange = (
            cq.Workplane("XY")
            .rect(100, 100)
            .extrude(self.material_thickness)
            .edges("|Z").fillet(15)
        )
        
        # Flange mounting holes
        for x in [-40, 40]:
            for y in [-40, 40]:
                flange = (
                    flange.faces(">Z")
                    .workplane()
                    .center(x, y)
                    .hole(5.2)
                )
        
        joint = joint.union(flange)
        
        # Set screw holes
        for angle in [0, 120, 240]:
            joint = (
                joint.faces(">Z")
                .workplane()
                .center(
                    base_diameter/2 * cq.cos(angle * cq.pi/180),
                    base_diameter/2 * cq.sin(angle * cq.pi/180)
                )
                .hole(3, base_height/2)  # M3 set screw
            )
        
        return joint
    
    def create_emergency_stop_mount(self):
        """Mount for big red emergency stop button"""
        # Main body
        mount = (
            cq.Workplane("XY")
            .rect(70, 50)
            .extrude(self.material_thickness)
        )
        
        # Button hole (standard E-stop is 22mm)
        mount = (
            mount.faces(">Z")
            .hole(22.5)
        )
        
        # Mounting wings
        for x in [-30, 30]:
            wing = (
                cq.Workplane("XY")
                .center(x, 0)
                .rect(20, 50)
                .extrude(self.material_thickness)
            )
            mount = mount.union(wing)
            
            # Mounting holes
            mount = (
                mount.faces(">Z")
                .workplane()
                .center(x, 0)
                .hole(5.2)
            )
        
        # Round edges for safety
        mount = mount.edges("|Z").fillet(5)
        
        return mount

# Generate all heavy parts
if __name__ == "__main__":
    print("Generating Dolly heavy duty parts...")
    
    heavy_parts = DollyHeavyParts()
    
    # Generate each part
    parts = [
        ("main_base_plate", heavy_parts.create_main_base_plate()),
        ("motor_mount_plate", heavy_parts.create_motor_mount_plate()),
        ("mac_mini_security_plate", heavy_parts.create_mac_mini_security_plate()),
        ("power_station_bracket", heavy_parts.create_power_station_bracket()),
        ("arm_base_joint", heavy_parts.create_arm_base_joint()),
        ("emergency_stop_mount", heavy_parts.create_emergency_stop_mount())
    ]
    
    for name, part in parts:
        cq.exporters.export(part, f"heavy_parts/dolly_{name}.step")
        cq.exporters.export(part, f"heavy_parts/dolly_{name}.stl")
        print(f"  ✓ {name}")
    
    print("\nHeavy parts generated in hardware/step/heavy_parts/")
    print("\nMaterial recommendations:")
    print("  - 6mm aluminum plate (best)")
    print("  - 1/4 inch aluminum (imperial equivalent)")
    print("  - 8-10mm PETG if 3D printing")
    print("  - 100% infill for 3D printed versions")
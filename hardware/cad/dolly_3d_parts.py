#!/usr/bin/env python3
"""
Dolly Robot - 3D Printed Parts Collection
Organized by category with multiple design options.
This is where creativity happens - customize your Dolly!
"""

import cadquery as cq
import math

# ==============================================================================
# PERSONALITY SHELLS - Make Dolly look like anything!
# ==============================================================================

class PersonalityShells:
    """Different aesthetic shells for Dolly's head and body"""
    
    def create_classic_head(self):
        """Classic robot look - think 1950s sci-fi"""
        head = (
            cq.Workplane("XY")
            .box(120, 100, 80)
            .edges("|Z").fillet(15)
        )
        
        # Antenna holes
        head = (
            head.faces(">Z")
            .workplane()
            .pushPoints([(-30, 0), (30, 0)])
            .hole(6)  # For springy antennas
        )
        
        # Eye visor slot
        head = (
            head.faces(">Y")
            .workplane()
            .center(0, 20)
            .slot2D(80, 15, 0)
            .cutThruAll()
        )
        
        return head
    
    def create_friendly_head(self):
        """Cute, approachable design - think WALL-E"""
        # Rounded main shape
        head = (
            cq.Workplane("XY")
            .sphere(60)
            .intersect(
                cq.Workplane("XY").box(120, 100, 80)
            )
        )
        
        # Big friendly eyes
        for x in [-25, 25]:
            eye = (
                cq.Workplane("XZ")
                .center(x, 20)
                .circle(20)
                .extrude(-10)
            )
            head = head.cut(eye)
        
        # Smile indent
        head = (
            head.faces(">Y")
            .workplane()
            .center(0, -10)
            .threePointArc((30, -20), (0, -25))
            .close()
            .cutBlind(-5)
        )
        
        return head
    
    def create_industrial_head(self):
        """Functional, no-nonsense design"""
        head = (
            cq.Workplane("XY")
            .box(100, 90, 70)
            .edges("|Z").chamfer(5)
        )
        
        # Sensor mounting rails
        rail_profile = (
            cq.Workplane("YZ")
            .polygon([(0, 0), (10, 0), (10, 5), (5, 10), (0, 10)])
        )
        
        for x in [-45, 45]:
            rail = rail_profile.extrude(60).translate((x, 0, 35))
            head = head.union(rail)
        
        # Ventilation grilles
        for i in range(5):
            head = (
                head.faces(">X")
                .workplane(offset=-10 - i*10)
                .slot2D(60, 3, 0)
                .cutThruAll()
            )
        
        return head
    
    def create_retro_futuristic_head(self):
        """Art deco meets robotics"""
        # Main dome
        head = (
            cq.Workplane("XY")
            .ellipse(60, 50)
            .extrude(40)
            .faces(">Z")
            .workplane()
            .ellipse(60, 50)
            .workplane(offset=40)
            .ellipse(40, 35)
            .loft()
        )
        
        # Chrome strips (indents for metallic tape)
        for angle in [0, 45, 90, 135]:
            strip = (
                cq.Workplane("XY")
                .center(
                    55 * math.cos(math.radians(angle)),
                    55 * math.sin(math.radians(angle))
                )
                .rect(5, 80)
                .extrude(1)
                .rotate((0, 0, 0), (0, 0, 1), angle)
            )
            head = head.cut(strip)
        
        return head

# ==============================================================================
# FUNCTIONAL COMPONENTS - Core 3D printed parts
# ==============================================================================

class FunctionalParts:
    """Essential 3D printed components"""
    
    def create_cable_chain_link(self):
        """Single link for cable management chain"""
        # Main body
        link = (
            cq.Workplane("XY")
            .rect(20, 30)
            .extrude(15)
            .edges("|X").fillet(2)
        )
        
        # Hollow center
        link = (
            link.faces(">Z")
            .rect(16, 26)
            .cutThruAll()
        )
        
        # Pin holes
        link = (
            link.faces(">Y")
            .workplane()
            .center(-7.5, 0)
            .hole(3)
            .center(15, 0)
            .hole(3)
        )
        
        # Snap features
        link = (
            link.faces(">X")
            .workplane()
            .center(0, 7.5)
            .circle(1.5)
            .extrude(5)
        )
        
        return link
    
    def create_encoder_wheel(self):
        """Wheel encoder disk for odometry"""
        wheel = (
            cq.Workplane("XY")
            .circle(40)
            .extrude(2)
        )
        
        # Encoder slots
        num_slots = 20
        for i in range(num_slots):
            angle = i * 360 / num_slots
            slot = (
                cq.Workplane("XY")
                .center(
                    30 * math.cos(math.radians(angle)),
                    30 * math.sin(math.radians(angle))
                )
                .rect(5, 10)
                .cutThruAll()
                .rotate((0, 0, 0), (0, 0, 1), angle)
            )
            wheel = wheel.cut(slot)
        
        # Center hole for shaft
        wheel = wheel.faces(">Z").hole(6)
        
        # Set screw flat
        wheel = (
            wheel.faces(">Z")
            .workplane()
            .center(3, 0)
            .rect(6, 3)
            .cutBlind(-1)
        )
        
        return wheel
    
    def create_sensor_mount_universal(self):
        """Adjustable mount for various sensors"""
        # Base
        mount = (
            cq.Workplane("XY")
            .rect(40, 30)
            .extrude(5)
        )
        
        # Sensor platform
        platform = (
            cq.Workplane("XY")
            .center(0, -15)
            .rect(30, 20)
            .extrude(3)
            .edges("|Z").fillet(2)
        )
        mount = mount.union(platform.translate((0, 0, 5)))
        
        # Adjustment slots
        for y in [-10, 10]:
            mount = (
                mount.faces(">Z")
                .workplane()
                .center(0, y)
                .slot2D(20, 4, 0)
                .cutThruAll()
            )
        
        # Common sensor mounting patterns
        # HC-SR04 ultrasonic
        mount = (
            mount.faces(">Z")
            .workplane(offset=5)
            .pushPoints([(-13, -15), (13, -15)])
            .hole(2)
        )
        
        return mount

# ==============================================================================
# GRIPPER DESIGNS - Different styles for different tasks
# ==============================================================================

class GripperDesigns:
    """Various gripper finger designs"""
    
    def create_circuit_gripper_fingers(self):
        """Precision fingers for handling components"""
        finger = (
            cq.Workplane("XY")
            .moveTo(0, 0)
            .lineTo(8, 0)
            .lineTo(6, 50)
            .lineTo(3, 60)
            .lineTo(0, 60)
            .close()
            .extrude(8)
        )
        
        # Soften edges
        finger = finger.edges("|Z").fillet(1)
        
        # Component groove
        finger = (
            finger.faces(">X")
            .workplane()
            .center(0, -55)
            .slot2D(3, 40, 90)
            .cutBlind(-2)
        )
        
        # Texture for grip (small pyramids)
        for i in range(5):
            grip = (
                cq.Workplane("XZ")
                .center(4, -50 + i*8)
                .rect(1, 1)
                .workplane(offset=1)
                .center(4, -50 + i*8)
                .point()
                .loft()
            )
            finger = finger.union(grip)
        
        # Pivot hole
        finger = (
            finger.faces(">Z")
            .workplane()
            .center(4, 5)
            .hole(3)
        )
        
        return finger
    
    def create_soft_gripper_fingers(self):
        """TPU fingers for delicate objects"""
        # Wider, padded design
        finger = (
            cq.Workplane("XY")
            .moveTo(0, 0)
            .lineTo(15, 0)
            .lineTo(12, 45)
            .spline([(10, 55), (5, 60), (0, 58)])
            .close()
            .extrude(12)
        )
        
        # Round all edges heavily
        finger = finger.edges().fillet(2)
        
        # Flex grooves
        for i in range(3):
            groove = (
                cq.Workplane("XZ")
                .center(7.5, -15 - i*12)
                .slot2D(8, 2, 0)
                .cutThruAll()
            )
            finger = finger.cut(groove)
        
        # Suction cup indents
        for i in range(4):
            cup = (
                cq.Workplane("XY")
                .center(6, -20 - i*10)
                .circle(3)
                .cutBlind(-1)
            )
            finger = finger.cut(cup)
        
        return finger
    
    def create_adaptive_gripper_palm(self):
        """Palm piece for adaptive gripping"""
        palm = (
            cq.Workplane("XY")
            .rect(50, 40)
            .extrude(15)
            .edges("|Z").fillet(5)
        )
        
        # Finger mounting slots
        for x in [-15, 0, 15]:
            slot = (
                cq.Workplane("XY")
                .center(x, 15)
                .rect(10, 8)
                .extrude(15)
            )
            palm = palm.cut(slot)
            
            # Pivot holes
            palm = (
                palm.faces(">X")
                .workplane()
                .center(-15 + x, 7.5)
                .hole(3)
            )
        
        # Servo mounting
        palm = (
            palm.faces("<Z")
            .rect(23, 12)
            .cutBlind(-10)
        )
        
        return palm

# ==============================================================================
# TOOL ATTACHMENTS - Expand Dolly's capabilities
# ==============================================================================

class ToolAttachments:
    """Quick-change tool attachments"""
    
    def create_vacuum_pickup_tool(self):
        """Vacuum pickup for SMD components"""
        # Main body
        tool = (
            cq.Workplane("XY")
            .circle(20)
            .extrude(40)
        )
        
        # Air inlet (side)
        tool = (
            tool.faces(">X")
            .workplane()
            .center(0, -10)
            .hole(6)  # For 6mm pneumatic fitting
        )
        
        # Vacuum channel
        tool = (
            tool.faces(">Z")
            .hole(4, 35)
            .faces(">Z")
            .workplane(offset=-35)
            .hole(1.5)  # Tiny hole for pickup
        )
        
        # Quick-change mount
        mount_plate = (
            cq.Workplane("XY")
            .rect(40, 40)
            .extrude(5)
            .edges("|Z").fillet(3)
            .translate((0, 0, -5))
        )
        
        # Mounting pattern
        mount_plate = (
            mount_plate.faces("<Z")
            .rect(30, 30, forConstruction=True)
            .vertices()
            .hole(3)
        )
        
        tool = tool.union(mount_plate)
        
        return tool
    
    def create_pen_holder(self):
        """Universal pen/marker holder"""
        # Split clamp design
        holder = (
            cq.Workplane("XY")
            .circle(15)
            .extrude(50)
        )
        
        # Pen hole (slightly tapered)
        holder = (
            holder.faces(">Z")
            .hole(10)
            .faces(">Z")
            .workplane(offset=-40)
            .hole(12)
        )
        
        # Split for clamping
        holder = (
            holder.faces(">Y")
            .workplane()
            .center(0, -25)
            .rect(2, 50)
            .cutThruAll()
        )
        
        # Clamping ears
        for x in [-15, 15]:
            ear = (
                cq.Workplane("XY")
                .center(x, 0)
                .rect(10, 20)
                .extrude(20)
                .translate((0, 0, 15))
            )
            holder = holder.union(ear)
            
            # Bolt holes
            holder = (
                holder.faces(">Y")
                .workplane()
                .center(x, -15)
                .hole(3)
            )
        
        # Mount base
        base = (
            cq.Workplane("XY")
            .rect(40, 40)
            .extrude(5)
            .edges("|Z").fillet(3)
        )
        holder = holder.union(base)
        
        return holder
    
    def create_camera_gimbal_mount(self):
        """2-axis gimbal for camera stabilization"""
        # Base mount
        base = (
            cq.Workplane("XY")
            .rect(50, 50)
            .extrude(10)
            .edges("|Z").fillet(5)
        )
        
        # Yaw servo mount
        yaw_mount = (
            cq.Workplane("XY")
            .rect(40, 20)
            .extrude(30)
            .translate((0, 0, 10))
        )
        base = base.union(yaw_mount)
        
        # Pitch arm (simplified)
        pitch_arm = (
            cq.Workplane("YZ")
            .moveTo(0, 0)
            .lineTo(40, 0)
            .lineTo(40, 30)
            .lineTo(30, 40)
            .lineTo(0, 40)
            .close()
            .extrude(10)
            .translate((-5, 0, 30))
        )
        
        # Camera mount plate
        camera_mount = (
            cq.Workplane("XZ")
            .rect(40, 30)
            .extrude(3)
            .translate((0, -35, 45))
        )
        
        # Standard camera mounting holes (1/4-20)
        camera_mount = (
            camera_mount.faces(">Y")
            .hole(6.35)  # 1/4 inch
        )
        
        gimbal = base.union(pitch_arm).union(camera_mount)
        
        return gimbal

# ==============================================================================
# DECORATIVE ELEMENTS - Make Dolly yours!
# ==============================================================================

class DecorativeElements:
    """Fun additions to personalize Dolly"""
    
    def create_led_ring_mount(self):
        """Mount for LED status ring"""
        ring = (
            cq.Workplane("XY")
            .circle(40)
            .circle(35)
            .extrude(5)
        )
        
        # Mounting tabs
        for angle in [0, 120, 240]:
            tab = (
                cq.Workplane("XY")
                .center(
                    45 * math.cos(math.radians(angle)),
                    45 * math.sin(math.radians(angle))
                )
                .rect(15, 10)
                .extrude(5)
                .edges("|Z").fillet(2)
            )
            ring = ring.union(tab)
            
            # Screw holes
            ring = (
                ring.faces(">Z")
                .workplane()
                .center(
                    45 * math.cos(math.radians(angle)),
                    45 * math.sin(math.radians(angle))
                )
                .hole(3)
            )
        
        # Wire channel
        ring = (
            ring.faces("<X")
            .workplane()
            .center(0, 2.5)
            .rect(5, 3)
            .cutThruAll()
        )
        
        return ring
    
    def create_nameplate(self):
        """Customizable nameplate"""
        plate = (
            cq.Workplane("XY")
            .rect(100, 30)
            .extrude(3)
            .edges("|Z").fillet(3)
        )
        
        # Text area (raised border)
        text_area = (
            cq.Workplane("XY")
            .rect(90, 20)
            .extrude(1)
            .translate((0, 0, 3))
        )
        plate = plate.union(text_area)
        
        # Mounting holes
        plate = (
            plate.faces(">Z")
            .workplane()
            .pushPoints([(-40, 0), (40, 0)])
            .hole(3)
        )
        
        # Add text in slicer or CAD software
        
        return plate
    
    def create_bow_tie(self):
        """Because every robot needs style"""
        # Bow tie shape
        bow = (
            cq.Workplane("XY")
            .moveTo(-30, 0)
            .lineTo(-10, 15)
            .lineTo(-10, -15)
            .close()
            .extrude(5)
        )
        
        # Mirror for other side
        bow = bow.union(bow.mirror("YZ"))
        
        # Center knot
        knot = (
            cq.Workplane("XY")
            .rect(15, 20)
            .extrude(8)
            .edges("|Z").fillet(2)
        )
        bow = bow.union(knot)
        
        # Mounting clip
        clip = (
            cq.Workplane("XY")
            .rect(20, 5)
            .extrude(15)
            .translate((0, -12.5, 0))
        )
        bow = bow.union(clip)
        
        return bow

# ==============================================================================
# MAIN GENERATION SCRIPT
# ==============================================================================

if __name__ == "__main__":
    print("Generating Dolly 3D printed parts collection...")
    print("=" * 50)
    
    # Create instances
    shells = PersonalityShells()
    functional = FunctionalParts()
    grippers = GripperDesigns()
    tools = ToolAttachments()
    decorative = DecorativeElements()
    
    # Generate all parts organized by category
    categories = {
        "personality_shells": [
            ("classic_head", shells.create_classic_head()),
            ("friendly_head", shells.create_friendly_head()),
            ("industrial_head", shells.create_industrial_head()),
            ("retro_futuristic_head", shells.create_retro_futuristic_head())
        ],
        "functional_parts": [
            ("cable_chain_link", functional.create_cable_chain_link()),
            ("encoder_wheel", functional.create_encoder_wheel()),
            ("sensor_mount_universal", functional.create_sensor_mount_universal())
        ],
        "gripper_designs": [
            ("circuit_gripper_fingers", grippers.create_circuit_gripper_fingers()),
            ("soft_gripper_fingers", grippers.create_soft_gripper_fingers()),
            ("adaptive_gripper_palm", grippers.create_adaptive_gripper_palm())
        ],
        "tool_attachments": [
            ("vacuum_pickup_tool", tools.create_vacuum_pickup_tool()),
            ("pen_holder", tools.create_pen_holder()),
            ("camera_gimbal_mount", tools.create_camera_gimbal_mount())
        ],
        "decorative_elements": [
            ("led_ring_mount", decorative.create_led_ring_mount()),
            ("nameplate", decorative.create_nameplate()),
            ("bow_tie", decorative.create_bow_tie())
        ]
    }
    
    # Export all parts
    for category, parts in categories.items():
        print(f"\n{category.replace('_', ' ').title()}:")
        for name, part in parts:
            filename = f"3d_parts/{category}/dolly_{name}"
            cq.exporters.export(part, f"{filename}.step")
            cq.exporters.export(part, f"{filename}.stl")
            print(f"  ✓ {name}")
    
    print("\n" + "=" * 50)
    print("All 3D printed parts generated!")
    print("\nPrinting recommendations:")
    print("  - PLA: Most parts (easy to print)")
    print("  - PETG: Structural parts (stronger)")
    print("  - TPU: Gripper fingers (flexible)")
    print("  - Layer height: 0.2mm standard, 0.1mm for detailed parts")
    print("  - Infill: 20-40% for most, 60%+ for load-bearing")
    print("\nCustomize these designs to make Dolly uniquely yours!")
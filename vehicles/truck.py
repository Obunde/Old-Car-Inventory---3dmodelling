from vpython import *
from .vehicles import Automobile

class Truck(Automobile):
    def __init__(self, make, model, mileage, price, load_capacity):
        super().__init__(make, model, mileage, price)
        self.load_capacity = load_capacity

    def display_3d(self, pos=vector(0, 0, 0), color_val=color.orange):
        scene.background = color.white
        scene.title = f"{self.make} {self.model}"

        render_list = []

        # Dimensions
        wheel_radius = 0.5
        wheel_length = 0.2
        cabin_length = 3
        cabin_height = 2
        cabin_width = 2

        cargo_length = 5
        cargo_height = 1.5
        cargo_width = 2

        # Cabin (Front)
        cabin = box(pos=pos + vector(-cargo_length/2 + cabin_length/2, cabin_height/2, 0),
                    size=vector(cabin_length, cabin_height, cabin_width),
                    color=color_val)
        render_list.append(cabin)

        # Cargo bed (Rear)
        cargo = box(pos=pos + vector(cargo_length/2 - cargo_length/2, cargo_height/2, 0),
                    size=vector(cargo_length, cargo_height, cargo_width),
                    color=color_val)
        render_list.append(cargo)

        # Headlights
        headlight_radius = 0.15
        headlight_y = pos.y + cabin_height * 0.6
        headlight_x = pos.x - cargo_length / 2 - headlight_radius
        headlight_z_offset = cabin_width / 3

        left_headlight = sphere(pos=vector(headlight_x, headlight_y, pos.z + headlight_z_offset),
                                radius=headlight_radius, color=color.yellow, emissive=True)
        right_headlight = sphere(pos=vector(headlight_x, headlight_y, pos.z - headlight_z_offset),
                                 radius=headlight_radius, color=color.yellow, emissive=True)
        render_list += [left_headlight, right_headlight]

        # Wheels (6)
        wheel_positions = [
            vector(-cargo_length/2 + 0.5, 0, cargo_width/2),
            vector(-cargo_length/2 + 0.5, 0, -cargo_width/2 - wheel_length),
            vector(0, 0, cargo_width/2),
            vector(0, 0, -cargo_width/2 - wheel_length),
            vector(cargo_length/2 - 0.5, 0, cargo_width/2),
            vector(cargo_length/2 - 0.5, 0, -cargo_width/2 - wheel_length)
        ]

        for wp in wheel_positions:
            wheel = cylinder(pos=pos + wp,
                             axis=vector(0, 0, wheel_length),
                             radius=wheel_radius,
                             color=color.black)
            render_list.append(wheel)

        # Flowers in front
        num_flowers = 6
        spacing = 1.5
        start_x = -((num_flowers - 1) * spacing) / 2
        for j in range(num_flowers):
            flower_x = start_x + j * spacing
            flower_z = cargo_width * 1.5
            flower_y = 0

            flower_center = cylinder(
                pos=vector(flower_x, flower_y, flower_z),
                axis=vector(0, 0, 0.05),
                radius=0.05,
                color=color.green
            )
            render_list.append(flower_center)

            for i in range(5):
                angle = 2 * pi / 5 * i
                offset = vector(cos(angle) * 0.15, sin(angle) * 0.15, 0)
                petal = ellipsoid(
                    pos=vector(flower_x, flower_y, flower_z) + offset,
                    length=0.15,
                    height=0.1,
                    width=0.05,
                    color=color.red,
                    axis=offset
                )
                render_list.append(petal)

            stem = cylinder(
                pos=vector(flower_x, flower_y, flower_z),
                axis=vector(0, -0.5, 0),
                radius=0.01,
                color=color.green
            )
            render_list.append(stem)

        # Label
        truck_label = label(pos=pos + vector(0, cabin_height + 0.5, 0),
                            text=f"{self.make} {self.model}\nLoad: {self.load_capacity}kg\nKsh {self.price}",
                            height=12, box=False, color=color_val)
        render_list.append(truck_label)

        return render_list

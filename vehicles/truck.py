from vpython import *
from .vehicles import Automobile
import random

class Truck(Automobile):
    def __init__(self, make, model, mileage, price, load_capacity):
        super().__init__(make, model, mileage, price)
        self.load_capacity = load_capacity

    def display_3d(self, pos=vector(0, 0, 0)):
        scene.background = color.white
        scene.title = f"{self.make} {self.model}"

        color_val = vector(random.random(), random.random(), random.random())
        render_list = []

        # Dimensions
        wheel_radius = random.uniform(0.4, 0.6)
        wheel_length = random.uniform(0.15, 0.25)

        cabin_length = random.uniform(2.5, 3.5)
        cabin_height = random.uniform(2.5, 3.5)
        truck_width = random.uniform(1.8, 2.5)

        cargo_length = random.uniform(4.5, 6)
        cargo_height = random.uniform(1.2, 2)

        # Cabin (Front)
        cabin = box(pos=pos + vector(-cargo_length/2 + cabin_length/2, cabin_height/2, 0),
                    size=vector(cabin_length, cabin_height, truck_width),
                    color=color_val)
        render_list.append(cabin)

        # Cargo bed (Rear)
        cargo = box(pos=pos + vector(cargo_length/2 - cargo_length/2, cargo_height/2, 0),
                    size=vector(cargo_length, cargo_height, truck_width),
                    color=color_val)
        render_list.append(cargo)

        # Cabin windows
        window_color = vector(0.5, 0.8, 1)
        window_opacity = 0.5

        window_thickness = 0.05
        window_height = cabin_height * 0.5
        window_length = cabin_length * 0.8
        window_width = truck_width * 0.4

        # Front window
        front_window = box(
            pos=cabin.pos + vector(-cabin_length / 2 - window_thickness / 2, cabin_height * 0.75 - window_height , 0),
            size=vector(window_thickness, window_height, truck_width * 0.9),
            color=window_color,
            opacity=window_opacity
        )
        render_list.append(front_window)

        # Side windows (left and right)
        for side in [1, -1]:
            side_window = box(
                pos=cabin.pos + vector(0, cabin_height * 0.75 - window_height , side * (truck_width / 2 + window_thickness / 2)),
                size=vector(window_length, window_height, window_thickness),
                color=window_color,
                opacity=window_opacity
            )
            render_list.append(side_window)

        # Headlights
        headlight_radius = 0.15
        headlight_y = pos.y + cabin_height * 0.2
        headlight_x = pos.x - cargo_length / 2 - headlight_radius
        headlight_z_offset = truck_width / 3

        left_headlight = sphere(pos=vector(headlight_x, headlight_y, pos.z + headlight_z_offset),
                                radius=headlight_radius, color=color.yellow, emissive=True)
        right_headlight = sphere(pos=vector(headlight_x, headlight_y, pos.z - headlight_z_offset),
                                 radius=headlight_radius, color=color.yellow, emissive=True)
        render_list += [left_headlight, right_headlight]

        # Wheels (6)
        wheel_positions = [
            vector(-cargo_length/2 + 0.5, 0, truck_width/2),
            vector(-cargo_length/2 + 0.5, 0, -truck_width/2 - wheel_length),
            vector(0, 0, truck_width/2),
            vector(0, 0, -truck_width/2 - wheel_length),
            vector(cargo_length/2 - 0.5, 0, truck_width/2),
            vector(cargo_length/2 - 0.5, 0, -truck_width/2 - wheel_length)
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
            flower_z = truck_width * 1.5
            flower_y = 0

            flower_center = cylinder(
                pos=vector(flower_x, flower_y, flower_z),
                axis=vector(0, 0, 0.05),
                radius=0.05,
                color=vector(random.random(), random.random(), random.random())
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
                    color=vector(random.random(), random.random(), random.random()),
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

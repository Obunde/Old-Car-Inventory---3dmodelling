from vpython import *
from .vehicles import Automobile # Adjusted for typical script usage

class SUV(Automobile):
    def __init__(self, make, model, mileage, price, doors):
        super().__init__(make, model, mileage, price)
        self.doors = doors

    def display_3d(self, pos=vector(0, 0, 0), color_val=color.red, render_list=None):
        if render_list is None:
            render_list = []

        scene.background = color.white
        scene.title = f"{self.make} {self.model}"

        # Dimensions
        wheel_radius = 0.5
        wheel_length = 0.12
        lower_body_length = 6
        lower_body_width = 2.5
        lower_body_height = 2
        upper_body_length = 4
        upper_body_width = 2.5
        upper_body_height = 1.5

        # Lower body
        lower_body = box(pos=pos + vector(0, lower_body_height / 2, 0),
                         size=vector(lower_body_length, lower_body_height, lower_body_width),
                         color=color_val)
        render_list.append(lower_body)

        # Upper body
        upper_body = box(pos=pos + vector(0, lower_body_height + upper_body_height / 2, 0),
                         size=vector(upper_body_length, upper_body_height, upper_body_width),
                         color=color_val)
        render_list.append(upper_body)

        # Windows
        window_color = color.white
        opacity = 0.5
        window_length = upper_body_length / 2 * 0.8
        window_thickness = 0.05
        window_height = upper_body_height * 0.9

        wind_screen = box(pos=upper_body.pos + vector(upper_body_length / 2 + window_thickness, 0, 0),
                          size=vector(window_thickness, window_height, upper_body_width * 0.9),
                          color=window_color, opacity=opacity)
        render_list.append(wind_screen)

        for side in [1, -1]:
            side_window1 = box(pos=upper_body.pos + vector(upper_body_length / 4, 0, side * (upper_body_width / 2 + window_thickness)),
                               size=vector(window_length, window_height, window_thickness),
                               color=window_color, opacity=opacity)
            side_window2 = box(pos=upper_body.pos + vector(-upper_body_length / 4, 0, side * (upper_body_width / 2 + window_thickness)),
                               size=vector(window_length, window_height, window_thickness),
                               color=window_color, opacity=opacity)
            render_list.extend([side_window1, side_window2])

        # Doors
        door_color = color.black
        door_opacity = 0.3
        door_length = upper_body_length / 2 * 0.9
        door_thickness = 0.05
        door_height = lower_body_height * 0.9

        for side in [1, -1]:
            door1 = box(pos=lower_body.pos + vector(upper_body_length / 4, 0.1, side * (lower_body_width / 2 + door_thickness)),
                        size=vector(door_length, door_height, door_thickness),
                        color=door_color, opacity=door_opacity)
            door2 = box(pos=lower_body.pos + vector(-upper_body_length / 4, 0.1, side * (lower_body_width / 2 + door_thickness)),
                        size=vector(door_length, door_height, door_thickness),
                        color=door_color, opacity=door_opacity)
            render_list.extend([door1, door2])

        # Headlights
        headlight_radius = 0.12
        headlight_y = pos.y + lower_body_height * 0.6
        headlight_x = pos.x + lower_body_length / 2 + headlight_radius * 0.5
        headlight_z_offset = lower_body_width / 3

        for side in [1, -1]:
            headlight = sphere(pos=vector(headlight_x, headlight_y, pos.z + side * headlight_z_offset),
                               radius=headlight_radius,
                               color=color.yellow,
                               emissive=True)
            render_list.append(headlight)

        # Wheels
        wheel_positions = [
            vector(-lower_body_length / 2 + wheel_radius * 2, 0, lower_body_width / 2),
            vector(-lower_body_length / 2 + wheel_radius * 1.5, 0, -lower_body_width / 2 - wheel_length),
            vector(lower_body_length / 2 - wheel_radius * 1.5, 0, lower_body_width / 2),
            vector(lower_body_length / 2 - wheel_radius * 1.5, 0, -lower_body_width / 2 - wheel_length)
        ]

        for wp in wheel_positions:
            wheel = cylinder(pos=wp, axis=vector(0, 0, wheel_length),
                             radius=wheel_radius, color=color.black)
            render_list.append(wheel)

        # Flowers
        num_flowers = 6
        spacing = 1.8
        start_x = -((num_flowers - 1) * spacing) / 2

        for j in range(num_flowers):
            flower_x = start_x + j * spacing
            flower_z = lower_body_width * 1.5
            flower_y = 0

            flower_center = cylinder(
                pos=vector(flower_x, flower_y, flower_z),
                axis=vector(0, 0, 0.05),
                radius=0.06,
                color=color.green
            )
            render_list.append(flower_center)

            for i in range(5):
                angle = (2 * pi / 5) * i
                offset = vector(cos(angle) * 0.15, sin(angle) * 0.15, 0)
                petal = ellipsoid(
                    pos=flower_center.pos + vector(0, 0.0125, 0) + offset,
                    length=0.15,
                    height=0.1,
                    width=0.05,
                    color=color.red,
                    axis=offset
                )
                render_list.append(petal)

            stem = cylinder(pos=flower_center.pos,
                            axis=vector(0, -0.5, 0),
                            radius=0.01,
                            color=color.green)
            render_list.append(stem)

        # Label
        label_obj = label(pos=pos + vector(0, lower_body_height + upper_body_height + 0.5, 0),
                          text=f"{self.make} {self.model}\nKsh {self.price}",
                          height=12, box=False, color=color_val)
        render_list.append(label_obj)

        return render_list

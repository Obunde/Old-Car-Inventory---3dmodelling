from vpython import *
from .vehicles import Automobile  # Adjusted import path
import random

class Car(Automobile):
    def __init__(self, make, model, mileage, price, doors):
        super().__init__(make, model, mileage, price)
        self.doors = doors

    def display_3d(self, pos=vector(0, 0, 0)):
        scene.background = color.white
        scene.title = f"{self.make} {self.model}"

        render_list = []  # List to hold current 3D objects for clearing

        color_val = vector(random.random(), random.random(), random.random())
        # Dimensions
        wheel_radius = random.uniform(0.3, 0.5)
        wheel_length = random.uniform(0.08, 0.12)

        lower_body_length = random.uniform(4.5, 6)
        car_width = random.uniform(1.8, 2.5)
        lower_body_height = random.uniform(1.2, 2)

        upper_body_length = random.uniform(2.5, 3.5)
        upper_body_height = random.uniform(0.8, 1.5)

        # Lower body of the car
        lower_body = box(pos=pos + vector(0, lower_body_height / 2, 0),
                         size=vector(lower_body_length, lower_body_height, car_width),
                         color=color_val)
        render_list.append(lower_body)

        # Upper body of the car
        upper_body = box(pos=pos + vector(0, lower_body_height + upper_body_height / 2, 0),
                         size=vector(upper_body_length, upper_body_height, car_width),
                         color=color_val)
        render_list.append(upper_body)

        # Windows (Front and Side)
        window_color = color.white  
        opacity = 0.5  # Fully opaque
        window_length = upper_body_length / 2 * 0.8
        window_thickness = 0.05  # Thickness of the window
        window_height = upper_body_height * 0.9  # Height of the window

        # Front window
        wind_screen = box(pos=upper_body.pos + vector(upper_body_length / 2 + window_thickness, 0, 0),
                          size=vector(window_thickness, window_height * 0.9, car_width * 0.9),
                          color=window_color, opacity=opacity)
        render_list.append(wind_screen)

        # Left side window
        left_front_window = box(pos=upper_body.pos + vector(upper_body_length / 4, 0, car_width / 2 + window_thickness),
                                size=vector(window_length, window_height * 0.9, window_thickness),
                                color=window_color, opacity=opacity)
        render_list.append(left_front_window)

        left_back_window = box(pos=upper_body.pos + vector(-upper_body_length / 4, 0, car_width / 2 + window_thickness),
                               size=vector(window_length, window_height * 0.9, window_thickness),
                               color=window_color, opacity=opacity)
        render_list.append(left_back_window)

        # Right side window
        right_front_window = box(pos=upper_body.pos + vector(upper_body_length / 4, 0, -car_width / 2 - window_thickness),
                                 size=vector(window_length, window_height * 0.9, window_thickness),
                                 color=window_color, opacity=opacity)
        render_list.append(right_front_window)

        right_back_window = box(pos=upper_body.pos + vector(-upper_body_length / 4, 0, -car_width / 2 - window_thickness),
                                size=vector(window_length, window_height * 0.9, window_thickness),
                                color=window_color, opacity=opacity)
        render_list.append(right_back_window)

        # Doors
        door_color = color.black
        door_opacity = 0.3
        door_length = upper_body_length / 2 * 0.9
        door_thickness = 0.05
        door_height = lower_body_height * 0.9

        for side in [1, -1]:
            door1 = box(pos=lower_body.pos + vector(upper_body_length / 4, 0.1, side * (car_width / 2 + door_thickness)),
                        size=vector(door_length, door_height, door_thickness),
                        color=door_color, opacity=door_opacity)
            door2 = box(pos=lower_body.pos + vector(-upper_body_length / 4, 0.1, side * (car_width / 2 + door_thickness)),
                        size=vector(door_length, door_height, door_thickness),
                        color=door_color, opacity=door_opacity)
            render_list.extend([door1, door2])

        # Headlights (Flashlights)
        headlight_radius = 0.1
        headlight_color = color.yellow
        headlight_y = pos.y + lower_body_height * 0.6  # slightly above middle of lower body
        headlight_x = pos.x + lower_body_length / 2 + headlight_radius * 0.5  # just in front of car
        headlight_z_offset = car_width / 3

        left_headlight = sphere(pos=vector(headlight_x, headlight_y, pos.z + headlight_z_offset),
                                radius=headlight_radius,
                                color=headlight_color,
                                emissive=True)
        render_list.append(left_headlight)

        right_headlight = sphere(pos=vector(headlight_x, headlight_y, pos.z - headlight_z_offset),
                                 radius=headlight_radius,
                                 color=headlight_color,
                                 emissive=True)
        render_list.append(right_headlight)

        # Wheels
        front_left_wheel = cylinder(pos=vector(-lower_body_length / 2 + (wheel_radius * 2), 0, car_width / 2),
                                    axis=vector(0, 0, wheel_length),
                                    radius=wheel_radius,
                                    color=color.black)
        render_list.append(front_left_wheel)

        front_right_wheel = cylinder(pos=vector(-lower_body_length / 2 + (wheel_radius * 1.5), 0, -car_width / 2 - wheel_length),
                                     axis=vector(0, 0, wheel_length),
                                     radius=wheel_radius,
                                     color=color.black)
        render_list.append(front_right_wheel)

        rear_left_wheel = cylinder(pos=vector(lower_body_length / 2 - (wheel_radius * 1.5), 0, car_width / 2),
                                   axis=vector(0, 0, wheel_length),
                                   radius=wheel_radius,
                                   color=color.black)
        render_list.append(rear_left_wheel)

        rear_right_wheel = cylinder(pos=vector(lower_body_length / 2 - (wheel_radius * 1.5), 0, -car_width / 2 - wheel_length),
                                    axis=vector(0, 0, wheel_length),
                                    radius=wheel_radius,
                                    color=color.black)
        render_list.append(rear_right_wheel)

        # Flower Line
        num_flowers = 6
        spacing = 1.5  # Space between each flower
        start_x = -((num_flowers - 1) * spacing) / 2  # Center the line

        for j in range(num_flowers):
            flower_x = start_x + j * spacing
            flower_z = car_width * 1.5  # A little in front of the car
            flower_y = 0

            # Flower Center
            flower_center_pos = vector(flower_x, flower_y, flower_z)
            flower_center = cylinder(pos=flower_center_pos, axis=vector(0, 0, 0.05),
                                     radius=0.05, color=vector(random.random(), random.random(), random.random()))
            render_list.append(flower_center)

            # Flower Petals
            for i in range(5):
                petal_angle = (2 * pi / 5) * i
                x = cos(petal_angle) * 0.15
                y = sin(petal_angle) * 0.15
                offset = vector(x, y, 0)

                petal = ellipsoid(pos=flower_center_pos + offset,
                                  length=0.15, height=0.1, width=0.05,
                                  color=vector(random.random(), random.random(), random.random()))
                render_list.append(petal)

            # Flower Stem
            stem = cylinder(pos=flower_center_pos, axis=vector(0, -0.5, 0),
                            radius=0.01, color=color.green)
            render_list.append(stem)

        # Label
        render_list.append(label(pos=pos + vector(0, lower_body_height + upper_body_height + 0.5, 0),
                                 text=f"{self.make} {self.model}\nKsh {self.price}",
                                 height=12, box=False, color=color_val))

        return render_list

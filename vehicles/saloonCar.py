from vpython import *
from .vehicles import Automobile

class Car(Automobile):
    def __init__(self, make, model, mileage, price, doors):
        super().__init__(make, model, mileage, price)
        self.doors = doors

    def display_3d(self, pos=vector(0, 0, 0), color_val=color.blue):
        scene.background = color.white
        scene.title = f"{self.make} {self.model}"

        # Dimensions
        wheel_radius = 0.4
        wheel_length = 0.1
        lower_body_length = 5
        lower_body_width = 2
        lower_body_height = 1.5
        upper_body_length = 3
        upper_body_width = 2
        upper_body_height = 1

        # Lower body of the car
        lower_body = box(pos=pos + vector(0, lower_body_height / 2, 0),
                         size=vector(lower_body_length, lower_body_height, lower_body_width),
                         color=color_val)

        # Upper body of the car
        upper_body = box(pos=pos + vector(0, lower_body_height + upper_body_height / 2, 0),
                         size=vector(upper_body_length, upper_body_height, upper_body_width),
                         color=color_val)

        # ============================
        # Windows (Front and Side)
        # ============================
        window_color = color.white  
        opacity = 0.5  # Fully opaque
        window_legnth = upper_body_length/2*0.8
        window_thickness = 0.05  # Thickness of the window
        window_height = upper_body_height*0.9  # Height of the window

        # Front window
        wind_screen = box(pos=upper_body.pos + vector(upper_body_length/2 +window_thickness , 0, 0),
                           size=vector(window_thickness, window_height*0.9,upper_body_width * 0.9),
                           color=window_color, opacity=opacity)

        # Left side window
        left_font_window = box(pos=upper_body.pos + vector(upper_body_length/4, 0, upper_body_width / 2 + window_thickness),
                          size=vector(window_legnth, window_height*0.9, window_thickness),
                          color=window_color, opacity=opacity)
        
        left_back_window = box(pos=upper_body.pos + vector(-upper_body_length/4, 0, upper_body_width / 2 + window_thickness),
                          size=vector(window_legnth, window_height*0.9, window_thickness),
                          color=window_color, opacity=opacity)

       # right side window
        right_font_window = box(pos=upper_body.pos + vector(upper_body_length/4, 0, -upper_body_width / 2 - window_thickness),
                          size=vector(window_legnth, window_height*0.9, window_thickness),
                          color=window_color, opacity=opacity)
        
        right_back_window = box(pos=upper_body.pos + vector(-upper_body_length/4, 0, -upper_body_width / 2 - window_thickness),
                          size=vector(window_legnth, window_height*0.9, window_thickness),
                          color=window_color, opacity=opacity)


        # ============================
        # door panes
        # ============================
        door_color = color.black   
        opacity = 0.3 
        door_legnth = upper_body_length/2*0.9
        door_thickness = 0.05  # Thickness of the window
        door_height = lower_body_height*0.9 # Height of the window


        # Left side doors
        left_font_door = box(pos=lower_body.pos + vector(upper_body_length/4, 0.1, lower_body_width / 2 + door_thickness),
                          size=vector(window_legnth, door_height*0.9, door_thickness),
                          color=door_color, opacity=opacity)
        
        left_back_door = box(pos=lower_body.pos + vector(-upper_body_length/4, 0.1, lower_body_width / 2 + door_thickness),
                          size=vector(window_legnth, door_height*0.9, door_thickness),
                          color=door_color, opacity=opacity)

       # right side window
        right_font_door = box(pos=lower_body.pos + vector(upper_body_length/4, 0.1, -lower_body_width / 2 - door_thickness),
                          size=vector(window_legnth, door_height*0.9, door_thickness),
                          color=door_color, opacity=opacity)
        
        right_back_door = box(pos=lower_body.pos + vector(-upper_body_length/4, 0.1, -lower_body_width / 2 - door_thickness),
                          size=vector(window_legnth, door_height, door_thickness),
                          color=door_color, opacity=opacity)


        # ============================
        # Headlights (Flashlights)
        # ============================
        headlight_radius = 0.1
        headlight_color = color.yellow

        headlight_y = pos.y + lower_body_height * 0.6  # slightly above middle of lower body
        headlight_x = pos.x + lower_body_length / 2 + headlight_radius * 0.5  # just in front of car
        headlight_z_offset = lower_body_width / 3

        left_headlight = sphere(
            pos=vector(headlight_x, headlight_y, pos.z + headlight_z_offset),
            radius=headlight_radius,
            color=headlight_color,
            emissive=True
        )

        right_headlight = sphere(
            pos=vector(headlight_x, headlight_y, pos.z - headlight_z_offset),
            radius=headlight_radius,
            color=headlight_color,
            emissive=True
        )

        # ============================
        # Wheels (already fixed)
        # ============================
        front_left_wheel = cylinder(
            pos=vector(-lower_body_length/2+(wheel_radius*2), 0, lower_body_width/2),
            axis=vector(0, 0, wheel_length),
            radius=wheel_radius,
            color=color.black
        )

        front_right_wheel = cylinder(
            pos=vector(-lower_body_length/2+(wheel_radius*1.5), 0, -lower_body_width/2-wheel_length),
            axis=vector(0, 0, wheel_length),
            radius=wheel_radius,
            color=color.black
        )

        rear_left_wheel = cylinder(
            pos=vector(lower_body_length/2-(wheel_radius*1.5), 0, lower_body_width/2),
            axis=vector(0, 0, wheel_length),
            radius=wheel_radius,
            color=color.black
        )

        rear_right_wheel = cylinder(
            pos=vector(lower_body_length/2-(wheel_radius*1.5), 0, -lower_body_width/2-wheel_length),
            axis=vector(0, 0, wheel_length),
            radius=wheel_radius,
            color=color.black
        )

        
        # ============================
        # Flower Parameters
        # ============================
        flower_center_radius = 0.05
        flower_center_thickness = 0.05
        flower_center_color = color.green

        flower_petal_color = color.red
        flower_petal_length = 0.15
        flower_petal_width = 0.1

        num_petals = 5

        

        # ============================
        # Flower Center
        # ============================
        flower_center_pos = vector(0, 0, lower_body_width * 2)
        flower_center = cylinder(
            pos=flower_center_pos,
            axis=vector(0, 0, flower_center_thickness),
            radius=flower_center_radius,
            color=flower_center_color
        )

        # ============================
        # Flower Petals
        # ============================
        for i in range(num_petals):
            angle = (2 * pi / num_petals) * i
            x = cos(angle) * flower_petal_length
            y = sin(angle) * flower_petal_length
            offset = vector(x, y, 0)  
            
            petal = ellipsoid(
                pos=flower_center_pos + vector(0, flower_center_thickness / 2, 0) + offset,
                length=flower_petal_length,
                height=flower_petal_width,
                width=flower_center_thickness,
                color=flower_petal_color,
                axis=offset
            )

        # ============================
        # Label
        # ============================
        label(pos=pos + vector(0, lower_body_height + upper_body_height + 0.5, 0),
              text=f"{self.make} {self.model}\nKsh {self.price}",
              height=12, box=False, color=color_val)

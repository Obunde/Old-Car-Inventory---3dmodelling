from vehicles.saloonCar import Car
from vehicles.truck import Truck
from vehicles.suv import SUV
from vpython import button, scene
from vpython import *

# Create objects
car = Car('BMW', 2001, 70000, 15000.0, 4)
truck = Truck('Toyota', 2002, 40000, 12000.0, '4WD')
suv = SUV('Volvo', 2000, 30000, 18500.0, 5)

# List to hold current 3D objects for clearing
current_objects = []

def clear_scene():
    global current_objects
    for obj in current_objects:
        obj.visible = False
        del obj
    current_objects = []

# Modified display_3d methods should accept `render_list` to store objects
def show_car():
    clear_scene()
    current_objects.extend(car.display_3d())
    info_display.text = car.display_info() 

def show_truck():
    clear_scene()
    current_objects.extend(truck.display_3d())
    info_display.text = truck.display_info() 

def show_suv():
    clear_scene()
    current_objects.extend(suv.display_3d())
    info_display.text = suv.display_info() 

info_display = wtext(text="")

# UI Buttons
button(text="Show Car", bind=lambda _: show_car())
button(text="Show Truck", bind=lambda _: show_truck())
button(text="Show SUV", bind=lambda _: show_suv())

# Keep window open
while True:
    pass
    

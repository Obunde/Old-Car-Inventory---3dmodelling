from vehicles.saloonCar import Car
from vehicles.truck import Truck
from vehicles.suv import SUV
from vpython import button, scene

# Create objects
car = Car('BMW', 2001, 70000, 15000.0, 4)
truck = Truck('Toyota', 2002, 40000, 12000.0, '4WD')
suv = SUV('Volvo', 2000, 30000, 18500.0, 5)

# Button actions
def show_car(): car.display_3d()
def show_truck(): truck.display_3d()
def show_suv(): suv.display_3d()

# UI Buttons
button(text="Show Car", bind=lambda _: show_car())
button(text="Show Truck", bind=lambda _: show_truck())
button(text="Show SUV", bind=lambda _: show_suv())

# Keep window open
while True:
    pass

from vpython import box, vector, color, label
from vehicles.vehicles import Automobile

class Truck(Automobile):
    def __init__(self, make, model, mileage, price, drive_type):
        super().__init__(make, model, mileage, price)
        self.drive_type = drive_type

    def display_3d(self):
        pos = vector(0, 0, 0)
        box(pos=pos, size=vector(5, 2, 2), color=color.green)
        label(pos=pos + vector(0, 1.5, 0),
              text=f"{self.make} {self.model}\nKsh {self.price}",
              height=12, box=False, color=color.green)

from vpython import box, vector, color, label
from vehicles.vehicles import Automobile

class SUV(Automobile):
    def __init__(self, make, model, mileage, price, pass_cap):
        super().__init__(make, model, mileage, price)
        self.pass_cap = pass_cap

    def display_3d(self):
        pos = vector(6, 0, 0)
        box(pos=pos, size=vector(4.5, 2, 2.5), color=color.blue)
        label(pos=pos + vector(0, 1.5, 0),
              text=f"{self.make} {self.model}\nKsh {self.price}",
              height=12, box=False, color=color.blue)

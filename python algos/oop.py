class Microwave:
    #dunder init function
    def __init__(self, brand: str, power_rating: str) -> None:
        #self references the instance of the object
        self.brand = brand
        self.power_rating = power_rating
        self.turned_on: bool = False
    
    def turn_on(self) -> None:
        if self.turned_on:
            print(f"{self.brand} microwave is already on")
        else:
            self.turned_on = True
            print(f"Turning on {self.brand}")
    
    def turn_off(self) -> None:
        if self.turned_on:
            self.turned_on = False
            print(f"Turning off {self.brand}")
        else:
            print(f"{self.brand} is already off")
    
    def run(self, seconds: int) -> None:
        if self.turned_on:
            print(f"Running {self.brand} for {seconds} seconds")
        else:
            print("Turn on microwave first!")

    def __add__(self, other):
        return f"{self.brand} + {other.brand}"
    
    def __str__(self):
        return f"({self.brand}, {self.power_rating})"
    
smeg: Microwave = Microwave("smeg", "B")
bosch: Microwave = Microwave('Bosch', "A")

print(smeg)
print(smeg + bosch)

# inheritance and subclasses
class Oven(Microwave):

    def turn_on(self) -> None:
        if self.turned_on:
            print(f"{self.brand} oven is already on")
        else:
            self.turned_on = True
            print(f"Turning on {self.brand}")

    def heating(self, temperature: int) -> str:
        return f'Heating food for at {temperature} degrees'

phillips: Oven = Oven("phillips", "A")
print(phillips.heating(40))
phillips.turn_on()
phillips.turn_on()
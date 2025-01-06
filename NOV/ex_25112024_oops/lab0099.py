class Car:

    def __init__(self, name, make, model):
        self.name = name
        self.make = make
        self.model = model
        print("before start ctor")

    def start_engine(self):
        print("Starting a car with the name " + self.name)
        print("Starting a car with the make " + self.make)
        print("Starting a car with the model " + self.model)


lambo = Car("Lambo", "V6", "2023")
lambo.start_engine()

INNOVA = Car("shift","v8","2")
INNOVA.start_engine()
print(" --- ")

mg_hector = Car("Hector","1.5+ Turbo","2024")
mg_hector.start_engine()
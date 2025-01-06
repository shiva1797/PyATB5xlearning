# Abstraction
# Hide the details and show what is required.


# Car - with key _ __private, tyres -> public,

# Car -> multiple - Engine, GearBox
# Car -> driver -> Engine, gearbox?


from abc import ABC,abstractmethod

class Animal(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def make_sound(self):
        print("im private")
        pass


class Dog(Animal):
    def make_sound(self):
        print("Bark Bark....")


obj_animal = Animal
obj_animal.make_sound("sound")
obj_dog = Dog("Shera")
obj_dog.make_sound()
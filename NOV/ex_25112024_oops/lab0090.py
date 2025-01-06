class Dog:
    # A
    name = None
    breed = None
    height = None
    weight = None

    # B
    def bark(self):
        print("Barking")

    def sleep(self):
        print("Sleep")

    def talk(self):
        pass


# Object Ref
obj = Dog()
obj.bark()

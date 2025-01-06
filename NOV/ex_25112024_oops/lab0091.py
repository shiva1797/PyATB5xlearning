class Dog:
    # Attributes - Instance variables | Data variables
    name = None
    breed = None
    height = None
    weight = None
    race = None


    def __init__(self, name, breed):
        print("PC")
        self.name = name
        self.breed = breed
        print(f"NAME:{name}|BREED:{breed}")

    def bark(self):
        print(self.name)

    def sleep(self):
        print("Who is sleep -> "+ self.name )

    def talk(self):
        pass


# Object Ref
obj = Dog("gaja","lab")
ob1 = Dog("PUP",'GERMAN')
obj.bark()
ob1.bark()
ob1.sleep()

#print(chow_ref.name)
#chow_ref.sleep()
#print(id(chow_ref))


#mow_ref = Dog()
#print(mow_ref.name)
#mow_ref.sleep()
#print(id(mow_ref))
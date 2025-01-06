# How to create a Class?
# Single Inheritance -> 85% of the time you will use SI in API, Web
class Father:
    key = "2BHK"
    def car(self):
        print("Father has a Car ->  Alto")
        print(self.key)

class Son(Father): # Single Inheritance
    key2 = "3BHK"

    def suv(self):
        print("MG Hector , Black")
        print(self.key2)

class sis(Son):
    key3 = "4bhk"
    def bmw(self):
        print("black bmw new series")
        pass


father_obj = Father()

father_obj.car()

son_obj = Son()
son_obj.suv()

sis_obj = sis()
sis_obj.bmw()
sis_obj.car()
sis_obj.suv()


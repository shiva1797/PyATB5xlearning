class dog:
    name= None
    age= None

    def __init__(self):
        print("i will be initiated")

    def call_me(self):
        print("you called me")

    def call_me_also(self):
        print("you call me also")


obj =dog()
obj1=dog()
obj.call_me_also()
obj1.call_me()
print(obj)
print(obj1)
# Encapsulation -
# Hide the data members(class variables, instance variables)
# by using only the methods.
from NOV.ex_25112024_oops.lab0100 import password


class Car:
    def __init__(self):
        self.password = "shiva" # public instance variable
        self.__password_secure = "pass123" # private instance variable

    def change_password(self):
        self.password1 ="1234"
       
        #self.__password_secure = "456"



object_ref = Car()
print(object_ref.password)
print(object_ref.password1)
object_ref.change_password()
#print(object_ref.__password_secure) # 'Car' object has no attribute '__password_secure'
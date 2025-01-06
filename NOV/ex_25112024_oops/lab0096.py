a = 29 #global


class Person:
    b = 20# Instance - Belong to class

    def print_info(self):
        c = 20  # Local variable
        print(c)
        print(self.b)
       
    def local_var(self):
        a=1000
        print(a)
        b=100
        print(self.b)


object_ref = Person()
object_ref.print_info()
object_ref.local_var()

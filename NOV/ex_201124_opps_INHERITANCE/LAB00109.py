# Multiple Inheritance
class A:
    def method(self):
        print("A")
        return "Method A"
class B:
    def method(self):
        print("B")


        return "Method B"
class C(B, A):
    pass

c = C()
print(c.method())
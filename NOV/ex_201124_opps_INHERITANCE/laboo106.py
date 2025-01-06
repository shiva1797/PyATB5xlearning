class Parent:
    gold = "2kg"

    def __init__(self):
        print("CTOR- Parent")

    def BHK2(self):
        print("2BHK")


class Child(Parent):

    def __init__(self):
        print("CTOR - Child")

    diamond = "Diamond"

    def BHK3(self):
        print("3BHK")

child_obj= Child()
print(child_obj.gold)
child_obj.BHK2()
child_obj.BHK3()


#parent_obj = Parent()
#parent_obj.BHK2()

# father_obect_ref.BHK3()
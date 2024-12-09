class shiva:
    name = None
    age= None
    def __init__(self):
        print("initialised CNTR")

    def print_data(self,name,age):
        self.name = name
        self.age = age
        print(f"NAME IS {name}\nAGE IS {age}")


    def one_more_print(self):
        print("one more funtion ")


obj = shiva()
obj.print_data("kumar",23)
obj.one_more_print()

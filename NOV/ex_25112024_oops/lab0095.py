class Calc:
    def __init__(self):
        print("DC")

    def sum(self,a,b):
        return a + b

    def sub(self,a,b):
        return a - b

    def mul(self,a,b):
        return a * b

    def div(self,a,b):
        return a / b


object_ref = Calc()


output_sum = object_ref.sum(6,7)
output_sub = object_ref.sub(66,77)
output_mul = object_ref.mul(5,8)
output_div = object_ref.div(7,9)
print(output_sum, output_sub, output_mul, output_div)
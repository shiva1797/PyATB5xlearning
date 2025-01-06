# Multilevel Inheritance
# GF -> F -> Son
# Multilevel Inheritance
class GrandFather:

    print("ctro GP")
    gold = "2kg"
    #print(gold)
    def bhk1(self):
        print("1BHK")

class Father(GrandFather):

    print("ctro F")
    diamond = "22 karat"
    def bhk2(self):
        print("2BHK")

class Son(Father):


    print("ctro S")
    btc = "1BTC"
    def bhk3(self):
        print("3BHK")


s = Son()
print(s.gold)
print(s.diamond)
print(s.btc)



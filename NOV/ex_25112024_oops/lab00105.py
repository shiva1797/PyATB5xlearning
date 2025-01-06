class Home:
    brother = "kiran"

    def __init__(self):
        self.public_var = "father"
        self.__private_var  = "child"
    def mom(self):
        print(self.__private_var)
        self.sis= "prathima"
        print( self.sis)
        self.__wife()

        #self.__wife()
    def __wife(self):
        print("im private")
        pass
#      print("Private Wife")
obj = Home()
obj.mom()

# object_ref.__wife()
# print(object_ref.__private_var) # 'Home' object has no attribute '__private_var'
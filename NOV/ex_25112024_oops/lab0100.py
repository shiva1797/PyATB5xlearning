# Web Automation - Selenium
# Page - You are going automate

class VWOLoginPage:

    def __init__(self, email_arg, password_arg):
        print("call CTOR")
        self.mail = email_arg
        self.pwd = password_arg

    def login_confirm(self):
        if self.mail == "pramod@gmail.com" and self.pwd == "Pass123":
            print("Allowed, Login Sucess")
        else:
            print("Login Failed")


email = input("Enter the email \n")
password = input("Enter the password \n")

vwo_obj = VWOLoginPage(email, password)
vwo_obj.login_confirm()

obj =VWOLoginPage()
obj()

obj1 =VWOLoginPage()
obj1()



pramod = VWOLoginPage("pramod@gmail.com", "Pass123")
pramod.login_confirm()
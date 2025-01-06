from enum import nonmember


class Bank:
    name = None
    def __init__(self, account_number, balance):
        print("i should call first")
        self.balance = balance  # Public
        self.__account_number = account_number  # Private

    def check_balance(self):
        print(self.balance)

    def deposit(self, amount):
        self.balance = self.balance + amount

    def public_function(self):
        self.__internal_private_method();

    def show_me_account_number(self, Auth):
        if Auth == True:
            print(self.__account_number)
        else:
            print("Not Allowed!")

    def __internal_private_method(self):
        print("Private Method, can be access by only Class")


icici = Bank(987654321017378383, 10299)
icici.check_balance()
icici.deposit(1)
icici.check_balance()
icici.show_me_account_number(True)
print(icici.balance)
# print(icici.__account_number)
#icici.show_me_account_number(False)
# icici.__internal_private_method()
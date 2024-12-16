class Bank:
    def __init__(self, account_number, balance):
        self.balance = balance   # Public
        self.__account_number = account_number # Private

    def check_balance(self):
        print(self.balance)

    def deposit(self, amount):
        self.balance = self.balance + amount

    def public_function(self):
        self.__internal_private_method()

    def show_me_account_number(self,is_auth):
        if is_auth == True:
            print(self.__account_number)
        else:
            print("You are not authorized")

    def __internal_private_method(self):
        print("Private method, can be accessed by only class")

icici = Bank(1828282828,100)
icici.deposit(100)
icici.check_balance()
print(icici.balance)
icici.show_me_account_number(False)
icici.show_me_account_number(True)
icici.public_function()
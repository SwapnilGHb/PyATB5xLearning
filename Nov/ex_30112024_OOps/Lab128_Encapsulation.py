# web Automation - Selenium
# Page - You are going automate

class VWOLoginPage:
    def __init__(self, email_arg,password_arg):
        self.email = email_arg
        self.password = password_arg


    def login_confirm(self):
        if self.email == "pramod@gmail.com" and self.password == "Pass123":
            print("Login Successful")
        else:
            print("Login Failed")


email = input("Enter the Email: \n")
password = input("Enter the Password: \n")

vmo_obj = VWOLoginPage(email,password)
vmo_obj.login_confirm()
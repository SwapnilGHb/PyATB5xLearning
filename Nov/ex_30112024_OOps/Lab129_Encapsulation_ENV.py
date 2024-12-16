# web Automation - Selenium
# Page - You are going automate
from dotenv import load_dotenv
import os

class VWOLoginPage:
    def __init__(self, email_arg,password_arg):
        self.email = email_arg
        self.password = password_arg


    def login_confirm(self):
        if self.email == "pramod@gmail.com" and self.password == "Pass123":
            print("Login Successful")
        else:
            print("Login Failed")

load_dotenv()

email = os.getenv("EMAIL")
password = os.getenv("PASSWORD")

print(email, password)

vmo_obj = VWOLoginPage(email,password)
vmo_obj.login_confirm()
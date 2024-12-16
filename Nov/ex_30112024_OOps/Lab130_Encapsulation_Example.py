# Encapsulation -
# Hide the data members(class variables, instance variables)
# by using only the methods

class Car:
    model = None
    name = None
    password = 123


    def __init__(self):
        self.password = "pramod"   # public instance variable
        self.__password_secure = "pass123" # private instance variable

    def change_password(self):
        print(self.password)

object_ref = Car()
print(object_ref.password)
print(object_ref.__password_secure)

object_ref.password = "Geeta"
object_ref.change_password()
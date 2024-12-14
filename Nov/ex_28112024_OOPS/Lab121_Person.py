# Take a input and create a class in Python

class Person:

    def __init__(self):
        print("I will be called")
        self.name = input("Enter your name\n")
        self.age = input("Enter your age\n")
        self.phone = input("Enter your phone number\n")
        self.occupation = input("Enter your occupation\n")

    def name_of_thr_function_to_display(self):
        print(f"Name is {self.name}",f"Age is {self.age} years old",f"Phone number is {self.phone}",f"Occupation is {self.occupation}")


person1 = Person()
person1.name_of_thr_function_to_display()
# User defined
# 1. They can't return -> non return
# 2. They can return something
# 3. They have parameters
# 4. They don't  have parameters / arguments
import math


# 1. They can't return -> non return
# No return type and no parameters/ argument - NRNP

def greet():
    print("Hello")

greet()

# 2. They can return something
# No return type with Argument - NRWP
def greet_by_name(name):
    print("Hello,",name)

greet_by_name("Pramod")


# 3. They have parameters
# No Return Type and with Default argument (# positional Argument
def say_hello_default_arg(name="Pramod"):
    print("Hello",name.upper())

say_hello_default_arg("Dutta")
say_hello_default_arg()

def multiple_args(name1="A",name2="B"):
    print("Mul",name1,name2)

multiple_args()
multiple_args("Lucky")
multiple_args(name1= "Pramod")
multiple_args(name1="Dutta",name2="Amit")
multiple_args(name2="Amit")

#4. Argument + return type

def sum_of_two(a,b):
    return a+b
result = sum_of_two(4,56)
print(result)


def sum_of_two_number_with_default(num1=100,num2=200):
    return num1+num2
result = sum_of_two_number_with_default(34,34)
print(result)
result = sum_of_two_number_with_default()
print(result)

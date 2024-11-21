# Problem to find the max between two

# logic building formula

# 1. user inputs -> two integers
# 2. o/p -> int 1 which ever is greater max number it will return
# 31.4 or 45.34 -> float

num1 = float(input("Enter the num1 :    "))
num2 = float(input("Enter the num2 :    "))

if num1>= num2:
    print("Maximum is  :", num1)
else:
    print("Maximum is   :",num2)

# Edge cases - num1 == num2 -> handled
# String -> ABC,ten -> try and except - we will learn this in future
# -ve value -> we will learn this in future

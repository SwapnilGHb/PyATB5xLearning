# Task for today
# Take a 2 input from the user
# print the Quotient and remainder
# 15 -> num1
# 2 -> num2
# Q - > 7
# R -> 1

num1 = int(input("Enter the num1 : " ))
num2 = int(input("Enter the num2 : " ))

quotient = int(num1//num2)
remainder = int(num1%num2)

print("The Quotient is :",quotient)
print("The Remainder is :",remainder)

# Create a program to sum of three number from the user input
# if user doesn't enter any number use default as 100,200,300


num1 = int(input("Enter the num1 \n  "))
num2 = int(input("Enter the num2 \n  "))
num3 = int(input("Enter the num3 \n  "))

def sum_of_three_numbers(num1=100,num2=200,num3=300):
    return num1+num2+num3

result = sum_of_three_numbers(num1,num2,num3)
print("Sum of user input three numbers :  ",result)

print("=============")
result2 = sum_of_three_numbers()
print("Sum of Default values of three numbers:  ",result2)


# # Write a program to calculate even and odd
#
# def find_even_odd(num):
#     if num % 2 == 0 :
#         print("Even")
#     else:
#         print("Odd")
#
# find_even_odd(10)

n = int(input("Enter a Num\n"))
check_Even_Odd = lambda num : "Even" if num % 2 == 0 else "Odd"
# print(check_Even_Odd(18))
# print(check_Even_Odd(10))
print(check_Even_Odd(n))
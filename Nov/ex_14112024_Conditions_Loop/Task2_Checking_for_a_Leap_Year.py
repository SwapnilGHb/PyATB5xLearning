# write a program Leap day occurs in each year
# that is a multiple of 4, except for years evenly
# divisible by 100 but not by 400.

year = int(input("Enter the year :    "))

if year%4 == 0:
    print("The year is leap year")
elif year%100==0 and year%400 !=0:
    print("The year is leap year")
else:
    print("The year is not leap year")
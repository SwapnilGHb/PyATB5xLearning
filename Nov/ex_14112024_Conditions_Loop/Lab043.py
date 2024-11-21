# Write a program to take a user age and
# let him know if he can go the club
# 21

# Logic Building formula

# Step 1
# User input i/p -> data type-> int
# o/p -> String -> user if he can go or not

# Step 2 Rough Logic (brute force : first thing came in mind)
# age > 21 -> print can go
# age < 21 -> print can't go

# Step 3 : Write the logic
age = input("Enter the Age \n")
age = int(age)

if age >= 21:
    print("Can go to club")
else:
    print("Can't go to club")

#Step 4 : Check for the edge cases
# we should consider edge cases such as :
# Negative ages or extremely high values -> program will break
# Non-numeric input - ABC
# Age which is valid


# Step 5 : Optimize the code
# Handle all the edge cases.

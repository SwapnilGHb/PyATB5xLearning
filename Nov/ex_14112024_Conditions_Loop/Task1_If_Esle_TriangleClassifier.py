# Write a program that classifies a triangle based
# on its side lengths. Given three input values
# representing the lengths of the sides, determine
# if the triangle is equilateral (all sides are equal),
# isosceles (exactly two sides are equal), or
# scalene (no sides are equal).
# Use an if-else statement to classify the triangle.


s1 = int(input("Enter the length of side1 :   "))
s2 = int(input("Enter the length of side2 :   "))
s3 = int(input("Enter the length of side3 :   "))

if s1 > 0 and s2 > 0 and s3 > 0:
    if s1 + s2 > s3 and s2 + s3 > s1 and s1 + s3 > s2:
        if s1 == s2 == s3:
            print("The Triangle is Equilateral triangle!")
        elif s1 == s2 or s2 == s3 or s1 == s3:
            print("The Triangle is Isosceles triangle!")
        elif s1 != s2 and s1 != s3 and s2 != s3:
            print("The Triangle is Scalene")
    else:
         print("Not a valid input")
else:
    print("Not a valid length!")

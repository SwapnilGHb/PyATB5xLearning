my_dict = {
    "name" : "Aman",
    "Age":"34",
    "role": "SDET",
    "experience": "3"
    }
print(my_dict)
print(my_dict["Age"])

my_dict["role"] = "Manual Tester"
print(my_dict)

del my_dict["Age"]
print(my_dict)

for key,value in my_dict.items():
    print(key, "->", value)

print("age" in my_dict)
print("role" in my_dict)


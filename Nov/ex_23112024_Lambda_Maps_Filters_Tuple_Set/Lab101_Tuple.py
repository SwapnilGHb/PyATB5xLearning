cities = ("London","Paris","LosAngeles","Tokyo")
print("Paris" in cities)
print("New Delhi" in cities)

t = (12,34,56)
# t.append(4) AttributeError: 'tuple' object has no attribute 'append'
my_list = list(t)
my_list.append(4)
t = tuple(my_list)
print(t)
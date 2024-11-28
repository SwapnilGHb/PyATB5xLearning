dict1 = {"a":1, "b" : 2, "c" : 3}
dict2 = {"a":1 , "b": 2}

missing_keys = set(dict1.keys()) - set(dict2.keys())
print(missing_keys)


# Sort a dictionary by its value in descending order
my_dict = {"a":3,"b": 1,"c":2}

sorted_by_values_asc = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=False))
print(sorted_by_values_asc)

sorted_by_values_desc = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))
print(sorted_by_values_desc)
# {"b":1,"c":2,"a":3}
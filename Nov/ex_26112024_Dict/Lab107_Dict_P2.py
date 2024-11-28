student_infor = {
    "name" : "Pramod",
    #"age" : 65,
    "age" : 67,
    "address": "KA"
}

print(student_infor["name"])
print(student_infor["age"])
print(student_infor["address"])
print("======")
student_infor["age"] =100
print(student_infor["age"])
print(student_infor)

student_infor = dict(name="Pramod",age = 67,address = "KA")
print(student_infor)

student_infor = {
    "name" : "Pramod",
    #"age" : 65,
    "age" : 67,
    "address": {
        "home_address": "ND",
        "office_address": "KA"
         }
    }

print(student_infor)
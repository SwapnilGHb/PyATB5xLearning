class PyATB:
    name = None
    age = None
    gender = None
    address = None
    phone = None
    print("Using parameterized Constructor")

    def __init__(self, name, age, gender, address, phone):
        self.name = name
        self.age = age
        self.gender = gender
        self.address = address
        self.phone = phone


    def Print_student1_info(self):
        return self.name , self.age , self.gender , self.address , self.phone

    def Print_student2_info(self):
        return self.name , self.age , self.gender , self.address , self.phone

    def Print_student3_info(self):
        return self.name, self.age, self.gender, self.address, self.phone


obj_ref = PyATB("Manish",40,"Male","Pune",9898989898)
obj_ref2 = PyATB("Rahul",40,"Male","Mumbai",6767676767)
obj_ref3 = PyATB("Rani",30,"FeMale","Pune",5656565656)


output_student1_info = obj_ref.Print_student1_info()
output_student2_info = obj_ref2.Print_student2_info()
output_student3_info = obj_ref3.Print_student3_info()


print(output_student1_info)
print(output_student2_info)
print(output_student3_info)
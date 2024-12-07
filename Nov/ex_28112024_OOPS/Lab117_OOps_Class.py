class Person:
#Attributes :- What you have?
    id = None
    name = None
    age = None
    email = None
    height = None
    gender = None
    phone_no = None
    adreess = None

# Behaviour :- What you can do?
    def talk(self):
        print("I can talk")

    def sleep(self,name): # Arg with no N
        print("I am Method!!")
        print("Sleep",name)

    def sleep2(self):
        print("I am Method")
        return None
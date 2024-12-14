class Dog:
    # Attribute /Insatance variables/ Data Variables
    name = None
    breed = None
    height = None

    def __init__(self,name,breed):
        print("Parameterized Constructor")
        self.name = name
        self.breed = breed

    # Behaviour
    def bark(self): # 1st Argument everywhere
        print("Barking")

    def sleep(self):
        print("Who is sleeping -> ",self.name)

    def talk(self):
        pass

# Object Reference
chow_ref = Dog("chow","mastif")
print(chow_ref.name)
print(chow_ref.breed)
chow_ref.sleep()
print(id(chow_ref))

mow_ref = Dog("mow","husky")
print(mow_ref.name)
print(mow_ref.breed)
mow_ref.sleep()
print(id(mow_ref))


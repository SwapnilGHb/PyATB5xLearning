class Dog:
    # Attribute
    name = None
    breed = None
    height = None

    # Behaviour
    def bark(self): # 1st Argument everywhere
        print("Barking")

    def sleep(self):
        print("Sleep")

    def talk(self):
        pass

# Object Reference
chow_ref = Dog()
# Dog() - Obj
# Chow - Object Reference
mow_ref = Dog()
bow_ref = Dog()
rancho_ref = Dog()

print(chow_ref.name)
print(mow_ref.name)

class Dog:
    # Attribute
    name = None
    breed = None
    height = None

    def __init__(self):
        print("I will be called")

    # Behaviour
    def bark(self): # 1st Argument everywhere
        print("Barking")

    def sleep(self):
        print("Who is sleeping -> ")

    def talk(self):
        pass

# Object Reference
chow_ref = Dog()
print(chow_ref.name)


mow_ref = Dog()
print(mow_ref.name)



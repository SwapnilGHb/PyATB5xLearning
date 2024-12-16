class Person:

    def __init__(self, name):
        self.name = name

    def walk(self):
        return self.name

amit = Person('Amit')
pramod = Person('Pramod')
print(amit.name)
print(pramod.name )

print("Who is walking :", amit.walk())
print("Who is walking :", pramod.walk())
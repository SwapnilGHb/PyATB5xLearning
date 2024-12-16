a = 10

class Person:
    b = 11  # instance - Belongs to class

    def print_info(self):
        c = 20 # local variable
        print(c)   # print(self.c) - for a local variable you don't need self
        print(self.b)  # for only instance variable we need self
        #print(a)
        global a   # to invoke global value use keyword "global" before variable
        print(a)
        a = "hello"   # preference will be given to local variable over global variable
        print(a)

object_ref = Person()
object_ref.print_info()


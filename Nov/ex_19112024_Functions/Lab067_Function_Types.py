def say_hello():
    print("hello")

say_hello()

# functions with argument, parameters

def greet_by_name(name):
    print("Hello,",name)
    print(f"Hello,{name}")
greet_by_name("pramod")
greet_by_name(123)
greet_by_name(3.14)
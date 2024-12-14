class Calculator:

    def __init__(self, a, b):
        self.a = a
        self.b = b
        print("parameterized Constructor")

    def sum(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b

    def mul(self):
        return self.a * self.b

    def div(self):
        return self.a / self.b


obj_ref = Calculator(3,4)
#obj_ref2 = Calculator(3,4)
#obj_ref3 = Calculator(3,4)
#obj_ref4 = Calculator(3,4)

output_sum = obj_ref.sum()
output_sub = obj_ref.sub()
output_mul = obj_ref.mul()
output_div = obj_ref.div()

print(output_sum, output_sub, output_mul, output_div)
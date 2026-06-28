class Calculator:
    def __init__(self):
        self.num1, self.num2 = map(int, input("enter two numbers separated by space:").split())
        self.operation = input("enter operation (+,-,*,/):")

    def calculate(self):
        if self.operation == "+":
            return self.num1 + self.num2
        elif self.operation == "-":
            return self.num1 - self.num2
        elif self.operation == "*":
            return self.num1 * self.num2
        elif self.operation == "/":
            if self.num2 == 0:
                return "Undefined"
            else:
                return self.num1 / self.num2
        else:
            return "Invalid operator"
obj=Calculator()
print("Result:", obj.calculate())

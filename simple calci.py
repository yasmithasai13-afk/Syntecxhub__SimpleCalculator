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
            if self.num2 == 0 or self.num1==0:
                return "Undefined"
            else:
                return self.num1 / self.num2
        else:
            return "Invalid operator"
    def repeat(self):
        while True:
            repeat = input("Do you want to perform another calculation? (y/n): ").lower()
            if repeat == "y":
                obj = Calculator()
                print("Result:", obj.calculate())
            elif repeat == "n":
                print("Thank you for using the calculator. Goodbye!")
                break
            else:
                print("Invalid input. Please enter 'y' or 'n'.")
obj=Calculator()
print("Result:", obj.calculate())
obj.repeat()

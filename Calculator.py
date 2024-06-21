class Calculate():
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    
    def add(self):
        return self.num1 + self.num2
    
    def subtract(self):
        return self.num1 - self.num2
    
    def multiply(self):
        return self.num1 * self.num2
    
    def divide(self):
        return self.num1 / self.num2

while True:
    print("1) Add two numbers")
    print("2) Subtract two numbers")
    print("3) Multiply two numbers")
    print("4) Divide two numbers")
    print("5) Exit")
    n = int(input())
    if n == 1:
        n1 = float(input("Enter number 1 : "))
        n2 = float(input("Enter number 2 : "))
        calc = Calculate(n1,n2)
        print(calc.add())
    elif n == 2:
        n1 = float(input("Enter number 1 : "))
        n2 = float(input("Enter number 2 : "))
        calc = Calculate(n1,n2)
        print(calc.subtract())
    elif n == 3:
        n1 = float(input("Enter number 1 : "))
        n2 = float(input("Enter number 2 : "))
        calc = Calculate(n1,n2)
        print(calc.multiply())
    elif n == 4:
        n1 = float(input("Enter number 1 : "))
        n2 = float(input("Enter number 2 : "))
        calc = Calculate(n1,n2)
        print(calc.divide())
    elif n == 5:
        exit(0)
    else:
        print("Invalid Input")
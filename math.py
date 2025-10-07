# math.py

# 使用者輸入
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
choice = input("Enter choice (+,-,*,/): ")

# 函式定義
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero."
    return a / b

# 主程式
if choice == '+':
    print(f"Result: {add(num1, num2)}")
elif choice == '-':
    print(f"Result: {subtract(num1, num2)}")
elif choice == '*':
    print(f"Result: {multiply(num1, num2)}")
elif choice == '/':
    print(f"Result: {divide(num1, num2)}")
else:
    print("Invalid input")

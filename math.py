num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
choice = input("Enter choice (+,-,*,/): ")

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

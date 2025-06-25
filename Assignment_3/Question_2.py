a = float(input("\nEnter first number: "))
b = float(input("Enter second number: "))

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y if y != 0 else "Cannot divide by zero"

print("\n--- Basic Operations ---")
print("Addition      :", add(a, b))
print("Subtraction   :", subtract(a, b))
print("Multiplication:", multiply(a, b))
print("Division      :", divide(a, b))
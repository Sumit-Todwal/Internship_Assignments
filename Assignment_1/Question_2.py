#Code for calculator
a = int(input("Enter number1"))
b = int(input("Enter number2"))
print("\nResults of Calculations\n")
print("Addition", a+b)
print("Subtraction", a-b)
print("Multiplication", a*b)

if(b != 0):
    print("Division",a/b)
    print("Modulus",a%b)
else:
    print("Divison Can not possible")
    print("Modulus can not possible")
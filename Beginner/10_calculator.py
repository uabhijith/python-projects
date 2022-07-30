def oprn(a, b, c):
    if c == "+":
        return a + b
    elif c == "-":
        return a - b
    elif c == "*":
        return a * b
    elif c == "/":
        return a / b
    else:
        return "invalid operation"


again = "y"
a = int(input("Enter first number:"))
while again == "y":
    c = input("Enter the operation: + - * / \n ")
    b = int(input("Enter second number:"))
    result = oprn(a, b, c)
    print(f"Result:{result}")
    again = input("do you want to operate with the result? y or n\n").lower()
    a = result

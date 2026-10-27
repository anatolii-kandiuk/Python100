def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):   
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

continue_calculating = True
operators = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}
    
while continue_calculating:
    operation = input("What operation would you like to perform? (+, -, *, /): ").lower()
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    if operation in operators:
        result = operators[operation](num1, num2)
        print(f"The result of {num1} {operation} {num2} is {result}")
    else:
        print("Invalid operation. Please try again.")
        continue

    continue_input = input("Would you like to perform another calculation? (yes/no): ").lower()
    if continue_input != "yes":
        continue_calculating = False

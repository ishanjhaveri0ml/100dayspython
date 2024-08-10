def add(num1, num2):
    return num1 + num2


def sub(num1, num2):
    return num1 - num2


def mul(num1, num2):
    return num1 * num2


def div(num1, num2):
    return num1 / num2


operations = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div,
}

accumulated = True

num1 = float(input("Enter the first number: "))
while accumulated:
    for operator in operations:
        print(operator)
    symbol = input("Enter the operation: ")
    num2 = float(input("Enter the second number: "))
    answer = operations[symbol](num1, num2)
    print(f"{num1} {symbol} {num2} = {answer}")

    choice = input(f"Type 'Y' to continue calculation with {answer}, or 'N' to start a new calculation, 'C' to exit: ").upper()

    if choice == "Y":
        num1 = answer  # Continue with the current result
    elif choice == "N":
        num1 = float(input("Enter the first number: "))  # Start a new calculation
    elif choice == "C":

        accumulated = False  # Exit the loop if the input is invalid

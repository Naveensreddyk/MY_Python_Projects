import art
def add(n1, n2):
    return n1 + n2
def sub(n1, n2):
    return n1 - n2
def mul(n1, n2):
    return n1 * n2
def div(n1, n2):
    return n1 / n2
operations = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div,
}
def my_calculator():
    print(art.logo)
    first_number = float(input("What's your first number?\n"))
    operator = input("Choose the operator ----- '+' '-' '*' '/'\n")
    second_number = float(input("What's your second number?\n"))
    if operator in operations:
        result = operations[operator](first_number, second_number)
        print(f" The result is {result}")
    else:
        print("Invalid Operator")
        result = 0
    next_steps = input("Do you want to continue with the previous result? Type YES or NO\n").lower()
    while next_steps == "yes":
        operator = input("Choose the operator ----- '+' '-' '*' '/'\n")
        second_number = float(input("What's your second number?\n"))
        first_number = result
        result = operations[operator](first_number, second_number)
        print(f" The result is {result}")
        next_steps = input("Do you want to continue with the previous result? Type YES or NO\n").lower()
    if next_steps == "no":
        print("\n" * 100)
        my_calculator()
my_calculator()










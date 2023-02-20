def add(x):
    return x + input_number()


def subtract(x):
    return x - input_number()


def multiply(x):
    return x * input_number()


def divide(x):
    return x / input_number()


def clear(x):
    return 0


operations = {
    "+": add,
    "-":  subtract,
    "*":  multiply,
    "/":  divide,
    "clear": clear,
}


def input_number():
    return int(input("Add a number"))


def calculate():
    sum = 0
    while True:
        print("Start typing numbers or operation (+ - * / clear close)")
        input_field = input()
        print(input_field)
        if input_field == "close":
            return
        elif input_field in operations:
            sum = operations[input_field](sum)
        elif input_field.isnumeric() == False:
            print("Incorrect input")
        else:
            sum = int(str(sum) + input_field)
        print(sum)


calculate()

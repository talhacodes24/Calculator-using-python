## make a advance calculator
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def divide(x, y):
    return x / y

def multiply(x, y):
    return x * y

def process(num1, num2, operator):
    result = 0

    if operator == "+":
        result = add(num1, num2)
    elif operator == "-":
        result = subtract(num1, num2)
    elif operator == "*":
        result = multiply(num1, num2)
    elif operator == "/":
        result = divide(num1, num2)

    print(result)

def main():
    try:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        operator = input("Enter operator: ")

        if operator in ["+", "-", "*", "/"]:

            print("currect answer:")
        else:
            raise ValueError

    except ValueError:
        print('Error!')
        exit()

    else:
        process(num1, num2, operator)

main()

## finish my advance calculator
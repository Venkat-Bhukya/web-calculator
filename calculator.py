def add(x,y):
    return x + y
def subtract(x,y):
    return x - y
def multiply(x,y):
    return x*y
def divide(x,y):
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x/y

def main():
    print("Welcome to the Console Calculator")
    print("Operations: +,-,*,/")
    try:
            a = float(input("Enter the first number:"))
            op = input("Enter the operation(+,-,*,/):")
            b = float(input("Enter the second number:"))

            if op == "+":
                result = add(a,b)
            elif op == "-":
                result = subtract(a,b)
            elif op == "*":
                result = multiply(a,b)
            elif op == "/":
                result = divide(a,b)
            else:
                print('Invalid Operator')

            print(f"Result: {result}")
    except ValueError as e:
            print(f"Error: {e}")
if __name__ == "__main__":
    main()
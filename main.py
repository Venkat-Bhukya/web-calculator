from calculator import calc
from scraper.scraper import scrape_website

def main():
    print("Choose a mode:")
    print("1. Web Scraper")
    print("2. Calculator")
    choice = input("Enter choice (1/2): ")

    if choice == '1':
        url = input("Enter URL to scrape: ")
        tag = input("Enter HTML tag to extract (e.g., h1, a): ")
        scrape_website(url, tag)
    elif choice == '2':
        a = float(input("Enter first number: "))
        op = input("Enter operation (+, -, *, /): ")
        b = float(input("Enter second number: "))

        try:
            if op == '+':
                print(calc.add(a, b))
            elif op == '-':
                print(calc.subtract(a, b))
            elif op == '*':
                print(calc.multiply(a, b))
            elif op == '/':
                print(calc.divide(a, b))
        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    main()
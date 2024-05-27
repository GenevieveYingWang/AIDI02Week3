def print_menu():
    print("Welcome to the Simple Calculator!")
    print("Please select an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

def get_user_choice():
    return input("Enter your choice (1-5): ")

def get_numbers():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    return num1, num2

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error! Division by zero."
    return a / b

def main():
    while True:
        print_menu()
        choice = get_user_choice()

        if choice == '5':
            print("Thank you for using the Simple Calculator. Goodbye!")
            break

        num1, num2 = get_numbers()

        if choice == '1':
            print(f"The result of {num1} + {num2} is {add(num1, num2)}")
        elif choice == '2':
            print(f"The result of {num1} - {num2} is {subtract(num1, num2)}")
        elif choice == '3':
            print(f"The result of {num1} * {num2} is {multiply(num1, num2)}")
        elif choice == '4':
            print(f"The result of {num1} / {num2} is {divide(num1, num2)}")
        else:
            print("Invalid choice! Please select a valid option.")

if __name__ == "__main__":
    main()

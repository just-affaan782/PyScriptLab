def calculate_rectangle():
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    area = length * width
    perimeter = 2 * (length + width)
    print("Area of the rectangle:", area)
    print("Perimeter of the rectangle:", perimeter)

def calculate_square():
    number = float(input("Enter a number: "))
    square = number ** 2
    print("The square of", number, "is", square)

def reverse_number():
    number = int(input("Enter an integer number: "))
    reversed_number = int(str(number)[::-1])
    print("The reverse of", number, "is:", reversed_number)

def check_leap_year():
    year = int(input("Enter a year: "))
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(year, "is a leap year.")
    else:
        print(year, "is not a leap year.")

def print_prime_numbers():
    lower = int(input("Enter the lower range: "))
    upper = int(input("Enter the upper range: "))
    print("Prime numbers between", lower, "and", upper, "are:")
    for num in range(lower, upper + 1):
        if num > 1:
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    break
            else:
                print(num, end=" ")
    print()

def calculate_triangle_area():
    base = float(input("Enter the base of the triangle: "))
    height = float(input("Enter the height of the triangle: "))
    area = 0.5 * base * height
    print("The area of the triangle is:", area)

def calculate_factorial():
    number = int(input("Enter a number: "))
    factorial = 1
    if number < 0:
        print("Factorial is not defined for negative numbers.")
    else:
        for i in range(1, number + 1):
            factorial *= i
        print("The factorial of", number, "is:", factorial)

def main_menu():
    while True:
        print("\n--- PyScriptLab ---")
        print("1. Calculate Rectangle Area and Perimeter")
        print("2. Calculate Square of a Number")
        print("3. Reverse a Number")
        print("4. Check Leap Year")
        print("5. Print Prime Numbers in a Range")
        print("6. Calculate Triangle Area")
        print("7. Calculate Factorial of a Number")
        print("0. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            calculate_rectangle()
        elif choice == '2':
            calculate_square()
        elif choice == '3':
            reverse_number()
        elif choice == '4':
            check_leap_year()
        elif choice == '5':
            print_prime_numbers()
        elif choice == '6':
            calculate_triangle_area()
        elif choice == '7':
            calculate_factorial()
        elif choice == '0':
            print("Exiting PyScriptLab by Affaan. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()

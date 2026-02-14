"""
BMI Calculator Program

Calculates BMI from weight in pounds and height in inches.
Allows repeated calculations and displays a BMI table.
"""

def calculate_bmi(weight, height):

    return 703 * weight / (height ** 2)

def display_bmi_table():
    col_width = 6

    print("\nBMI TABLE")

    print("Weight".ljust(col_width), end="")
    for height in range(58, 77, 2):
        print(str(height).center(col_width), end="")
    print()

    for weight in range(100, 251, 10):
        print(str(weight).ljust(col_width), end="")
        for height in range(58, 77, 2):
            bmi = calculate_bmi(weight, height)
            print(f"{bmi:>{col_width}.1f}", end="")
        print()
def main():

    print("BMI Calculator")

    running = True
    while running:
        choice = input("\nEnter 'c' to calculate BMI, 't' to view BMI table, or 'q' to quit: ").lower()

        if choice == 'q':
            running = False
            continue
        elif choice == 't':
            display_bmi_table()
            continue
        elif choice != 'c':
            print("Invalid selection. Please enter 'c', 't', or 'q'.")
            continue

        while True:
            weight_input = input("Enter weight in pounds (or 'q' to quit): ")
            if weight_input.lower() == 'q':
                running = False
                break
            try:
                weight = float(weight_input)
                if weight <= 0:
                    print("Weight must be greater than zero.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a numeric value.")

        if not running:
            break

        while True:
            height_input = input("Enter height in inches (or 'q' to quit): ")
            if height_input.lower() == 'q':
                running = False
                break
            try:
                height = float(height_input)
                if height <= 0:
                    print("Height must be greater than zero.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a numeric value.")

        if not running:
            break

        bmi = calculate_bmi(weight, height)
        print(f"Your BMI is: {bmi:.2f}")

    print("Program ended.")

if __name__ == "__main__":
    main()

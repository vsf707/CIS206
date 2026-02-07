def main():
    try:
        # Get user input
        age = int(input("What is your age? "))
        membership = input("Enter membership type Basic or Premium: ").lower()

        # #1 Validation: range validation
        if age <= 0 or age > 100:
            print("Invalid age")
            return

        # #1 Validation: consistency validation
        if membership not in ["basic", "premium"]:
            print("Invalid membership type")
            return

        # #3 Nested if statement
        if membership == "premium":
            if age >= 60:
                discount = 20
            else:
                discount = 10
        else:
                discount = 0

        print("Your discount is:", discount, "%")

    # #2 Exception handling
    except ValueError:
        print("Age must be a number")

main()

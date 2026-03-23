import csv

def load_customers(filename):
    customers = []
    try:
        with open(filename, newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                for key in row:
                    if row[key] == "NULL":
                        row[key] = ""
                customers.append(row)
    except FileNotFoundError:
        print("Error: File not found.")
    return customers

def display_customers(customers):
    if not customers:
        print("No records found.")
        return

    for c in customers:
        print(f"Company Name: {c['CompanyName']}")
        print(f"Contact Name: {c['ContactName']}")
        print(f"Phone: {c['Phone']}")
        print("-" * 40)

def sort_by_company(customers):
    return sorted(customers, key=lambda x: x['CompanyName'].lower())

def sort_by_contact(customers):
    return sorted(customers, key=lambda x: x['ContactName'].lower())

def search_customers(customers, key, search_term):
    results = []
    search_term = search_term.lower()

    for c in customers:
        if search_term in c[key].lower():
            results.append(c)

    return results

def main():
    filename = "customers.csv"
    customers = load_customers(filename)

    if not customers:
        return

    while True:
        print("\n===== Customer Menu =====")
        print("1. Display sorted by Company Name")
        print("2. Display sorted by Contact Name")
        print("3. Search by Company Name")
        print("4. Search by Contact Name")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            sorted_list = sort_by_company(customers)
            display_customers(sorted_list)

        elif choice == "2":
            sorted_list = sort_by_contact(customers)
            display_customers(sorted_list)

        elif choice == "3":
            term = input("Enter company name or part: ").strip()
            if term:
                results = search_customers(customers, "CompanyName", term)
                display_customers(results)
            else:
                print("Invalid input.")

        elif choice == "4":
            term = input("Enter contact name or part: ").strip()
            if term:
                results = search_customers(customers, "ContactName", term)
                display_customers(results)
            else:
                print("Invalid input.")

        elif choice == "5":
            print("Exiting program...")
            break

        else:
            print("Invalid choice. Please enter 1-5.")

if __name__ == "__main__":
    main()

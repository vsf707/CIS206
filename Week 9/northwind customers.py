import csv
def load_customers(filename):

    customers = []

    try:
        with open(filename, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                company = row.get('CompanyName', '').strip()
                contact = row.get('ContactName', '').strip()
                phone = row.get('Phone', '').strip()
                if company and contact and phone:  # simple validation
                    customers.append((company, contact, phone))
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"Error reading file: {e}")

    return customers

def sort_customers(customers, key_index):

    return sorted(customers, key=lambda x: x[key_index])

def display_customers(customers, display_order):

    if display_order == 'company':
        sorted_list = sort_customers(customers, 0)
        print("\nCustomers Sorted by Company Name:\n")
        for company, contact, phone in sorted_list:
            print(f"Company: {company}\nContact: {contact}\nPhone: {phone}\n")
    elif display_order == 'contact':
        sorted_list = sort_customers(customers, 1)
        print("\nCustomers Sorted by Contact Name:\n")
        for company, contact, phone in sorted_list:
            print(f"Contact: {contact}\nCompany: {company}\nPhone: {phone}\n")
    else:
        print("Invalid display order.")

def search_customers(customers, search_field):

    search_term = input(f"\nEnter {search_field} name or part of name: ").strip().lower()
    if not search_term:
        print("Search term cannot be empty.")
        return

    matches = []
    index = 0 if search_field == 'company' else 1

    for customer in customers:
        if search_term in customer[index].lower():
            matches.append(customer)

    if matches:
        print(f"\nMatching {search_field.title()}s:\n")
        for company, contact, phone in matches:
            print(f"Company: {company}\nContact: {contact}\nPhone: {phone}\n")
    else:
        print(f"No matches found for '{search_term}'.")

def get_menu_choice():

    print("\nCustomer Menu")
    print("1. Display customers sorted by company name")
    print("2. Display customers sorted by contact name")
    print("3. Search customers by company name")
    print("4. Search customers by contact name")
    print("5. Exit")

    choice = input("Enter your choice: ").strip()
    if choice in {"1", "2", "3", "4", "5"}:
        return choice
    print("Invalid choice. Please enter 1-5.")
    return None

def main():

    filename = "northwind customers.txt"
    customers = load_customers(filename)

    if not customers:
        print("No customers loaded. Exiting.")
        return

    while True:
        choice = get_menu_choice()
        if choice is None:
            continue

        if choice == "1":
            display_customers(customers, 'company')
        elif choice == "2":
            display_customers(customers, 'contact')
        elif choice == "3":
            search_customers(customers, 'company')
        elif choice == "4":
            search_customers(customers, 'contact')
        elif choice == "5":
            print("Exiting program.")
            break

if __name__ == "__main__":
    main()

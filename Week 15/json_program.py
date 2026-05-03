import json

def load_books(filename):
    with open(filename, "r") as file:
        return json.load(file)

def display_books(data):
    print("\n--- Book List ---\n")

    for book in data["books"]:
        print("Title:", book["title"])
        print("Author:", book["author"])
        print("Year:", book["year"])
        print("Available:", book["available"])
        print("-" * 30)

def search_books(data):
    while True:
        user_input = input("\nEnter a book title (or type 'exit'): ")

        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        found = False

        for book in data["books"]:
            if book["title"].lower() == user_input.lower():
                print("\nBook Found:")
                print("Title:", book["title"])
                print("Author:", book["author"])
                print("Year:", book["year"])
                found = True
                break

        if not found:
            print("Title not found.")

def main():
    data = load_books("books.json")

    display_books(data)
    search_books(data)

if __name__ == "__main__":
    main()
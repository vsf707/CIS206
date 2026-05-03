import xml.etree.ElementTree as ET

def load_xml(filename):
    tree = ET.parse(filename)
    return tree.getroot()

def display_books(root):
    print("\n--- Book List (XML) ---\n")

    for book in root.findall("book"):
        print("Title:", book.find("title").text)
        print("Author:", book.find("author").text)
        print("Year:", book.find("year").text)
        print("Available:", book.find("available").text)
        print("-" * 30)

def search_books(root):
    while True:
        user_input = input("\nEnter a book title (or type 'exit'): ")

        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        found = False

        for book in root.findall("book"):
            title = book.find("title").text

            if title.lower() == user_input.lower():
                print("\nBook Found:")
                print("Title:", title)
                print("Author:", book.find("author").text)
                print("Year:", book.find("year").text)
                found = True
                break

        if not found:
            print("Title not found.")

def main():
    root = load_xml("books.xml")

    display_books(root)
    search_books(root)

if __name__ == "__main__":
    main()
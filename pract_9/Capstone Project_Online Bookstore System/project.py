import sqlite3
import csv
import os
# Database setup
def connect_db():
    conn = sqlite3.connect("bookstore.db")
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        author TEXT NOT NULL,
        price REAL NOT NULL,
        stock INTEGER NOT NULL
    )""")
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS customers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL
    )""")
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS orders (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        customer_id INTEGER,
        book_id INTEGER,
        quantity INTEGER,
        total_price REAL,
        order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (customer_id) REFERENCES customers(id),
        FOREIGN KEY (book_id) REFERENCES books(id)
    )""")
    conn.commit()
    conn.close()


# Add book to inventory
def add_book(title, author, price, stock):
    conn = sqlite3.connect("bookstore.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO books (title, author, price, stock) VALUES (?, ?, ?, ?)", (title, author, price, stock))
    conn.commit()
    conn.close()


# View books
def view_books():
    conn = sqlite3.connect("bookstore.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()
    conn.close()
    return books


# Place an order
def place_order(customer_name, customer_email, book_id, quantity):
    conn = sqlite3.connect("bookstore.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM customers WHERE email = ?", (customer_email,))
    customer = cursor.fetchone()

    if not customer:
        cursor.execute("INSERT INTO customers (name, email) VALUES (?, ?)", (customer_name, customer_email))
        conn.commit()
        customer_id = cursor.lastrowid
    else:
        customer_id = customer[0]

    cursor.execute("SELECT * FROM books WHERE id = ?", (book_id,))
    book = cursor.fetchone()
    if book and book[4] >= quantity:
        total_price = book[3] * quantity
        cursor.execute("INSERT INTO orders (customer_id, book_id, quantity, total_price) VALUES (?, ?, ?, ?)",
                       (customer_id, book_id, quantity, total_price))
        cursor.execute("UPDATE books SET stock = stock - ? WHERE id = ?", (quantity, book_id))
        conn.commit()
        print("Order placed successfully!")
    else:
        print("Insufficient stock or invalid book ID!")
    conn.close()


# Export book inventory to CSV
def export_inventory():
    conn = sqlite3.connect("bookstore.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()
    conn.close()

    with open("inventory.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Title", "Author", "Price", "Stock"])
        writer.writerows(books)
    print("Inventory exported successfully!")


# Import books from CSV
def import_books():
    if not os.path.exists("inventory.csv"):
        print("No inventory file found!")
        return

    conn = sqlite3.connect("bookstore.db")
    cursor = conn.cursor()
    with open("inventory.csv", "r") as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            cursor.execute("INSERT INTO books (id, title, author, price, stock) VALUES (?, ?, ?, ?, ?)", row)
    conn.commit()
    conn.close()
    print("Inventory imported successfully!")


# Interactive Menu
def menu():
    connect_db()
    while True:
        print("\n--- Online Bookstore System ---")
        print("1. Add Book")
        print("2. View Books")
        print("3. Place Order")
        print("4. Export Inventory")
        print("5. Import Inventory")
        print("6. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter author: ")
            price = float(input("Enter price: "))
            stock = int(input("Enter stock quantity: "))
            add_book(title, author, price, stock)
        elif choice == "2":
            books = view_books()
            for book in books:
                print(book)
        elif choice == "3":
            name = input("Enter your name: ")
            email = input("Enter your email: ")
            book_id = int(input("Enter book ID: "))
            quantity = int(input("Enter quantity: "))
            place_order(name, email, book_id, quantity)
        elif choice == "4":
            export_inventory()
        elif choice == "5":
            import_books()
        elif choice == "6":
            print("Exiting system...")
            break
        else:
            print("Invalid choice! Try again.")


if __name__ == "__main__":
    menu()

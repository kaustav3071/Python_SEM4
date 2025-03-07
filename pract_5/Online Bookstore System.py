class Books:
    def __init__(self, title, author, genre, price):
        self.__title = title
        self.__author = author
        self.__genre = genre
        self.__price = price

    def get_title(self):
        return self.__title

    def get_price(self):
        return self.__price

    def display(self):
        return (f"Title: {self.__title}\n"
                f"Author: {self.__author}\n"
                f"Genre: {self.__genre}\n"
                f"Price: ${self.__price}")


class EBooks(Books):
    def __init__(self, title, author, genre, price, file_size):
        super().__init__(title, author, genre, price)
        self.__file_size = file_size

    def display(self):
        return super().display() + f"\nFile Size: {self.__file_size}MB"


class PrintedBooks(Books):
    def __init__(self, title, author, genre, price, making_cost):
        super().__init__(title, author, genre, price)
        self.__making_cost = making_cost

    def display(self):
        return super().display() + f"\nMaking Cost: ${self.__making_cost}"

    def total_price(self):
        return self.get_price() + self.__making_cost


class CustomersOrders:
    def __init__(self, customer_name):
        self._CustomersOrders__books = None
        self.__customer_name = customer_name
        self.__books = []
        self.__total_price = 0
class Books:
    def __init__(self, title, author, genre, price):
        self.__title = title
        self.__author = author
        self.__genre = genre
        self.__price = price

    def get_title(self):
        return self.__title

    def get_price(self):
        return self.__price

    def display(self):
        return (f"Title: {self.__title}\n"
                f"Author: {self.__author}\n"
                f"Genre: {self.__genre}\n"
                f"Price: ${self.__price}")


class EBooks(Books):
    def __init__(self, title, author, genre, price, file_size):
        super().__init__(title, author, genre, price)
        self.__file_size = file_size

    def display(self):
        return super().display() + f"\nFile Size: {self.__file_size}MB"


class PrintedBooks(Books):
    def __init__(self, title, author, genre, price, making_cost):
        super().__init__(title, author, genre, price)
        self.__making_cost = making_cost

    def display(self):
        return super().display() + f"\nMaking Cost: ${self.__making_cost}"

    def total_price(self):
        return self.get_price() + self.__making_cost


class CustomersOrders:
    def __init__(self, customer_name):
        self.__customer_name = customer_name
        self.__books = []
        self.__total_price = 0

    def add_book(self, book):
        self.__books.append(book)
        self.__total_price += book.get_price()

    def order_summary(self):
        book_titles = [book.get_title() for book in self.__books]
        return (f"Customer Name: {self.__customer_name}\n"
                f"Books Ordered: {', '.join(book_titles)}\n"
                f"Total Price: ${self.__total_price}")


class Bookstore:
    def __init__(self):
        self.catalog = []
        self.total_revenue_amount = 0

    def add_book(self, book):
        self.catalog.append(book)

    def view_bookstore(self):
        if not self.catalog:
            return "No books available."
        return "\n".join([f"{i + 1}. {book.display()}" for i, book in enumerate(self.catalog)])

    def process_order(self, order):
        print("\nOrder Summary:\n")
        print(order.order_summary())
        self.total_revenue_amount += self.__calculate_order_total(order)

    def __calculate_order_total(self, order):
        total = sum(book.get_price() for book in order._CustomersOrders__books)
        return total

    def total_revenue(self):
        return f"\nTotal Revenue: ${self.total_revenue_amount}"


def main():
    print("Welcome to the Online Bookstore System!\n")

    bookstore = Bookstore()

    # Adding books to the catalog
    book1 = EBooks("The Hobbit", "J.R.R. Tolkien", "Fantasy", 15, 5)
    book2 = PrintedBooks("1984", "George Orwell", "Dystopian", 10, 3)
    book3 = PrintedBooks("To Kill a Mockingbird", "Harper Lee", "Fiction", 12, 4)
    book4 = EBooks("Sapiens", "Yuval Noah Harari", "History", 18, 6)

    bookstore.add_book(book1)
    bookstore.add_book(book2)
    bookstore.add_book(book3)
    bookstore.add_book(book4)

    # Taking customer order
    name = input("Enter your name: ")
    order = CustomersOrders(name)

    while True:
        print("\nBooks available:\n")
        print(bookstore.view_bookstore())

        try:
            choice = int(input("\nEnter the book number you want to order (0 to finish): ")) - 1

            if choice == -1:
                break
            elif 0 <= choice < len(bookstore.catalog):
                order.add_book(bookstore.catalog[choice])
                print(f"Added '{bookstore.catalog[choice].get_title()}' to your order.")
            else:
                print("Invalid selection! Please choose a valid book number.")

        except ValueError:
            print("Invalid input! Please enter a number.")

    # Process order if books were selected
    if order._CustomersOrders__books:
        bookstore.process_order(order)
    else:
        print("\nNo books were ordered.")

    # Display total revenue
    print(bookstore.total_revenue())


if __name__ == "__main__":
    main()

    def add_book(self, book):
        self.__books.append(book)
        self.__total_price += book.get_price()

    def order_summary(self):
        book_titles = [book.get_title() for book in self.__books]
        return (f"Customer Name: {self.__customer_name}\n"
                f"Books Ordered: {', '.join(book_titles)}\n"
                f"Total Price: ${self.__total_price}")


class Bookstore:
    def __init__(self):
        self.catalog = []
        self.total_revenue_amount = 0

    def add_book(self, book):
        self.catalog.append(book)

    def view_bookstore(self):
        if not self.catalog:
            return "No books available."
        return "\n".join([f"{i + 1}. {book.display()}" for i, book in enumerate(self.catalog)])

    def process_order(self, order):
        print("\nOrder Summary:\n")
        print(order.order_summary())
        self.total_revenue_amount += self.__calculate_order_total(order)

    def __calculate_order_total(self, order):
        total = sum(book.get_price() for book in order._CustomersOrders__books)
        return total

    def total_revenue(self):
        return f"\nTotal Revenue: ${self.total_revenue_amount}"


def main():
    print("Welcome to the Online Bookstore System!\n")

    bookstore = Bookstore()

    # Adding books to the catalog
    book1 = EBooks("The Hobbit", "J.R.R. Tolkien", "Fantasy", 15, 5)
    book2 = PrintedBooks("1984", "George Orwell", "Dystopian", 10, 3)
    book3 = PrintedBooks("To Kill a Mockingbird", "Harper Lee", "Fiction", 12, 4)
    book4 = EBooks("Sapiens", "Yuval Noah Harari", "History", 18, 6)

    bookstore.add_book(book1)
    bookstore.add_book(book2)
    bookstore.add_book(book3)
    bookstore.add_book(book4)

    # Taking customer order
    name = input("Enter your name: ")
    order = CustomersOrders(name)

    while True:
        print("\nBooks available:\n")
        print(bookstore.view_bookstore())

        try:
            choice = int(input("\nEnter the book number you want to order (0 to finish): ")) - 1

            if choice == -1:
                break
            elif 0 <= choice < len(bookstore.catalog):
                order.add_book(bookstore.catalog[choice])
                print(f"Added '{bookstore.catalog[choice].get_title()}' to your order.")
            else:
                print("Invalid selection! Please choose a valid book number.")

        except ValueError:
            print("Invalid input! Please enter a number.")


    if order._CustomersOrders__books:
        bookstore.process_order(order)
    else:
        print("\nNo books were ordered.")

    print(bookstore.total_revenue())


if __name__ == "__main__":
    main()

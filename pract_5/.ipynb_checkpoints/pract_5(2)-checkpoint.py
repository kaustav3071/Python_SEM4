class Book:
    def __init__(self, title, author, ISBN):
        self.__title = title
        self.__author = author
        self.__ISBN = ISBN

    @property
    def title(self):
        return self.__title

    @property
    def author(self):
        return self.__author

    @property
    def ISBN(self):
        return self.__ISBN

    @title.setter
    def title(self, title):
        if not title:
            raise ValueError("Title cannot be empty")
        self.__title = title

    @author.setter
    def author(self, author):
        if not author:
            raise ValueError("Author cannot be empty")
        self.__author = author

    @ISBN.setter
    def ISBN(self, ISBN):
        if not ISBN:
            raise ValueError("ISBN cannot be empty")
        self.__ISBN = ISBN

def main():
    print("Book class")
    book = Book("Python", "Kaustav", "123456789")
    print("Book Title is : ",book.title)
    print("Book Author is : ",book.author)
    print("Book ISBN Number is : ",book.ISBN)
    print()
    print("Setting book attributes")
    print()
    book.title = "Python for Beginners"
    book.author = "Kaustav Das"
    book.ISBN = "987654321"
    print("Book Title is : ",book.title)
    print("Book Author is : ",book.author)
    print("Book ISBN Number is : ",book.ISBN)

if __name__ == "__main__":
    main()

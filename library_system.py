#  The Base class
class Book:
    def __init__(self, title, author, pages):
        self.title = title          # Public attribute
        self.__author = author      # Private attribute (encapsulation is what this is)
        self.pages = pages

    def show_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.__author}")
        print(f"Pages: {self.pages}")

    def read(self):
        print(f"You are reading '{self.title}' by {self.__author}.")

# Inherited class
class EBook(Book):
    def __init__(self, title, author, pages, file_size):
        super().__init__(title, author, pages)
        self.file_size = file_size  # in MB

    def read(self):
        print(f"You are reading the eBook '{self.title}' ({self.file_size}MB) on your device!")

# Creating objects
book1 = Book("The Secret Garden", "Frances Hodgson Burnett", 300)
ebook1 = EBook("Digital Fortress", "Dan Brown", 356, 2)

book1.show_info()
book1.read()
print()
ebook1.show_info()
ebook1.read()

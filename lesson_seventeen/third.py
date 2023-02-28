# Create a Book class that has two attributes:

#     title
#     author

# and two methods:

#     A method named .get_title() that returns: "Title: " + the instance title.
#     A method named .get_author() that returns: "Author: " + the instance author.

# and instantiate this class by creating 3 new books:

#     Pride and Prejudice - Jane Austen (PP)
#     Hamlet - William Shakespeare (H)
#     War and Peace - Leo Tolstoy (WP)

# The name of the new instances should be PP, H, and WP, respectively. For instance, if I instantiated the following book using this Book class:

#     Harry Potter - J.K. Rowling (HP)
import logging  

logging.basicConfig(level=logging.DEBUG)


class Book:
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author
    def get_title(self) -> str:
        return "Title: " + self.title
    def get_author(self) -> str:
        return "Author: " + self.author

PP = Book("Pride and Prejudice", "Jane Austen")
H = Book("Hamlet", "William Shakespeare")
WP = Book("War and Peace", "Leo Tolstoy")

logging.debug(PP.get_author())
print(WP.get_author())
print(H.get_title())

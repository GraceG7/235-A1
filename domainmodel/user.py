from domainmodel.book import Book
from domainmodel.review import Review


class User:
    def __init__(self, name, user_password):
        self.__user_name = None
        self.__password = None
        if isinstance(name, str):
            self.__user_name = name.strip().lower()
        if len(user_password) >= 7:
            self.__password = user_password
        self.__read_books = []
        self.__reviews = []
        self.__pages_read = 0

    @property
    def user_name(self):
        return self.__user_name

    @property
    def password(self):
        return self.__password

    @property
    def read_books(self):
        return self.__read_books

    @property
    def reviews(self):
        return self.__reviews

    @property
    def pages_read(self):
        return self.__pages_read

    def __repr__(self):
        return f"<User {self.__user_name}>"

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__user_name == other.__user_name
        else:
            return False

    def __lt__(self, other):
        return self.__user_name < other.__user_name

    def __hash__(self):
        return hash(self.__user_name)

    def read_a_book(self, book):
        if isinstance(book, Book):
            if book not in self.__read_books:
                self.__read_books.append(book)
                self.__pages_read += book.num_pages

    def add_review(self, review):
        if isinstance(review, Review):
            self.__reviews.append(review)

import datetime

from domainmodel.book import Book


class Review:
    def __init__(self, abook, text, rate):
        if rate < 1 or rate > 5:
            raise ValueError
        if isinstance(abook, Book):
            self.__book = abook
        else:
            self.__book = None
        if isinstance(text, str):
            self.__review_text = text.strip()
        else:
            self.__review_text = "N/A"
        self.__rating = rate
        self.__timestamp = datetime.datetime.now()

    @property
    def book(self):
        return self.__book

    @property
    def review_text(self):
        return self.__review_text

    @property
    def rating(self):
        return self.__rating

    @property
    def timestamp(self):
        return self.__timestamp

    def __repr__(self):
        return "<Book {}, book id = {}>\nReview: {}\nRating: ".format(self.__book.title, self.__book.book_id, self.__review_text, self.__rating)

    def __eq__(self, other):
        if isinstance(other, Review):
            return self.__book == other.__book and self.__review_text == other.__review_text and self.__rating == other.__rating and self.__timestamp == other.__timestamp
        else:
            return False
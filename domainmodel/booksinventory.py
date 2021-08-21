class BooksInventory:

    def __init__(self):
        self.__data = {}

    def add_book(self, book, price, nr_books_in_stocks):
        book_id = book.book_id
        self.__data[book_id] = {}
        self.__data[book_id]["book"] = book
        self.__data[book_id]["price"] = price
        self.__data[book_id]["stock"] = nr_books_in_stocks

    def remove_book(self, book_id):
        if book_id in self.__data.keys():
            del self.__data[book_id]

    def find_book(self, book_id):
        if book_id in self.__data.keys():
            return self.__data[book_id]["book"]
        else:
            return None

    def find_price(self, book_id):
        if book_id in self.__data.keys():
            return self.__data[book_id]["price"]
        else:
            return None

    def find_stock_count(self, book_id):
        if book_id in self.__data.keys():
            return self.__data[book_id]["stock"]
        else:
            return None

    def search_book_by_title(self, title):
        for book_id in self.__data.keys():
            book_obj = self.__data[book_id]["book"]
            if book_obj.title == title:
                return book_obj
        return None
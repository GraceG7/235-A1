import json

from domainmodel.author import Author
from domainmodel.book import Book
from domainmodel.publisher import Publisher


class BooksJSONReader:

    def __init__(self, books_file_name: str, authors_file_name: str):
        # TODO
        self.__books_file_name = books_file_name
        self.__authors_file_name = authors_file_name
        self.__dataset_of_books = []

    @property
    def dataset_of_books(self) -> list:
        return self.__dataset_of_books

    def read_json_files(self):
        # TODO
        books_file = open(self.__books_file_name)
        authors_file = open(self.__authors_file_name)
        authors_dict = {}
        for a_json_obj in authors_file:
            author_data = json.loads(a_json_obj)
            if author_data["author_id"] not in authors_dict:
                authors_dict[author_data["author_id"]] = author_data["name"]
        for json_obj in books_file:
            books = json.loads(json_obj)
            addBook = Book(int(books["book_id"]), books["title"])
            addBook.publisher = Publisher(books["publisher"])
            addBook.description = books["description"]
            authors_list = []
            if books["num_pages"].isdigit():
                addBook.num_pages = int(books["num_pages"])
            for author in books["authors"]:
                id = author["author_id"]
                authors_list.append(Author(int(id), authors_dict[id]))
            addBook.authors = authors_list
            addBook.ebook = bool(books["is_ebook"])
            if books["publication_year"] != "":
                addBook.release_year = int(books["publication_year"])
            self.__dataset_of_books.append(addBook)

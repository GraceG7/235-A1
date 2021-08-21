from domainmodel.publisher import Publisher


class Book:
    def __init__(self, id, btitle):
        if isinstance(btitle, str) and isinstance(id, int):
            if btitle.strip() != "":
                self.__book_id = id
                self.__title = btitle.strip()
                self.__publisher = None
                self.__description = None
                self.__authors = []
                self.__release_year = None
                self.__ebook = None
                self.__num_pages = 0
            else:
                raise ValueError
        else:
            raise ValueError

    @property
    def book_id(self):
        return self.__book_id

    @property
    def title(self):
        return self.__title

    @property
    def publisher(self):
        return self.__publisher

    @property
    def description(self):
        return self.__description

    @property
    def authors(self):
        return self.__authors

    @property
    def release_year(self):
        return self.__release_year

    @property
    def ebook(self):
        return self.__ebook

    @property
    def num_pages(self):
        return self.__num_pages

    @title.setter
    def title(self, new_title):
        if isinstance(new_title, str):
            if new_title.strip() != "":
                self.__title = new_title.strip()
            else:
                raise ValueError
        else:
            raise ValueError

    @description.setter
    def description(self, desc):
        if isinstance(desc, str):
            self.__description = desc.strip()
        else:
            raise ValueError

    @publisher.setter
    def publisher(self, name):
        if isinstance(name, Publisher):
            self.__publisher = name
        else:
            raise ValueError

    @release_year.setter
    def release_year(self, year):
        if isinstance(year, int):
            if year >= 0:
                self.__release_year = year
            else:
                raise ValueError
        else:
            raise ValueError

    @authors.setter
    def authors(self, author_list):
        self.__authors = author_list

    @ebook.setter
    def ebook(self, b):
        self.__ebook = b

    @num_pages.setter
    def num_pages(self, pages):
        if isinstance(pages, int):
            if pages > 0:
                self.__num_pages = pages

    def __repr__(self):
        return "<Book {}, book id = {}>".format(self.__title, self.__book_id)

    def __eq__(self, other):
        return self.__book_id == other.__book_id

    def __lt__(self, other):
        return self.__book_id < other.__book_id

    def __hash__(self):
        return hash(self.__book_id)

    def add_author(self, new_author):
        if new_author not in self.__authors:
            self.__authors.append(new_author)

    def remove_author(self, remove_author):
        if remove_author in self.__authors:
            self.__authors.remove(remove_author)
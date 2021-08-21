class Author:

    def __init__(self, author_id, author_full_name):
        if isinstance(author_id, int) and isinstance(author_full_name, str):
            if author_id >= 0 and author_full_name.strip() != "":
                self.__unique_id = author_id
                self.__full_name = author_full_name.strip()
                self.__coAuthors = []
            else:
                raise ValueError
        else:
            raise ValueError

    @property
    def unique_id(self):
        return self.__unique_id

    @property
    def full_name(self):
        return self.__full_name

    @full_name.setter
    def full_name(self, name):
        if isinstance(name, str):
            if name.strip() != "":
                self.__full_name = name.strip()

    def __repr__(self):
        return "<Author {}, author id = {}>".format(self.__full_name, self.__unique_id)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__unique_id == other.__unique_id
        else:
            return False

    def __lt__(self, other):
        return self.__unique_id < other.__unique_id

    def __hash__(self):
        return hash(self.__unique_id)

    def add_coauthor(self, coauthor):
        self.__coAuthors.append(coauthor)

    def check_if_this_author_coauthored_with(self, author):
        return author in self.__coAuthors


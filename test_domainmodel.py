import pytest

from domainmodel.author import Author
from domainmodel.book import Book
from domainmodel.publisher import Publisher
from domainmodel.review import Review
from domainmodel.user import User


class TestUser:

    def test_constructor(self):
        user1 = User('Shyamli', 'pw12345')
        assert user1.user_name == 'shyamli'
        assert user1.password == 'pw12345'
        assert isinstance(user1.password, str)
        user2 = User('Susan', 'pw1234')
        assert user2.user_name == 'susan'
        assert user2.password is None
        user3 = User(1, 'pw1234')
        assert user3.user_name is None
        assert user3.read_books == []
        assert user3.reviews == []
        assert user3.pages_read == 0

    def test_eq_lt(self):
        user1 = User('Shyamli', 'pw12345')
        user3 = User('Shyamli', 'pw12346')
        user2 = User('Zebra', 'pw1234')
        assert not(user1 == user2)
        assert user1 == user3
        assert user1 < user2

    def test_read_book(self):
        user1 = User('Shyamli', 'pw12345')
        book1 = Book(874658, "Harry Potter")
        user1.read_a_book(book1)
        user1.read_a_book(book1)
        assert len(user1.read_books) == 2
        assert user1.read_books[0] == book1
        assert user1.pages_read == book1.num_pages * 2

    def test_reviews(self):
        user1 = User('Shyamli', 'pw12345')
        book1 = Book(874658, "Harry Potter")
        r1 = Review(book1, 'Good', 3)
        user1.add_review(r1)
        assert len(user1.reviews) == 1
        assert user1.reviews[0] == r1


class TestBook:

    def test_constructor(self):
        b1 = Book(84765876, "Harry Potter")
        id = b1.book_id
        name = b1.title
        assert id == 84765876
        assert name == "Harry Potter"
        assert str(b1) == "<Book Harry Potter, book id = 84765876>"

    def test_add_remove_authors(self):
        author = Author(635, "J.K. Rowling")
        b1 = Book(84765876, "Harry Potter")
        b1.add_author(author)
        assert len(b1.authors) == 1
        b1.remove_author(author)
        assert b1.authors == []

    def test_eq(self):
        b1 = Book(84765876, "Harry Potter2.0")
        b2 = Book(84765876, "Harry Potter2.1")
        b3 = Book(84765875, "Harry Potter3.0")
        assert b1 == b2
        assert not(b1 == b3)

    def test_lt(self):
        b2 = Book(84765876, "Harry Potter2.1")
        b3 = Book(84765875, "Harry Potter3.0")
        assert b3 < b2
        assert not(b2 < b3)

    def test_ebook_setter(self):
        b2 = Book(84765876, "Harry Potter2.1")
        b3 = Book(84765875, "Harry Potter3.0")
        assert b2.ebook is None
        b2.ebook = True
        b3.ebook = False
        assert b2.ebook
        assert not b3.ebook


class TestPublisher:

    def test_construction(self):
        publisher1 = Publisher("Avatar Press")
        assert str(publisher1) == "<Publisher Avatar Press>"
        publisher2 = Publisher("  ")
        assert str(publisher2) == "<Publisher N/A>"
        publisher3 = Publisher("  DC Comics ")
        assert str(publisher3) == "<Publisher DC Comics>"
        publisher4 = Publisher(42)
        assert str(publisher4) == "<Publisher N/A>"

    def test_equal(self):
        publisher1 = Publisher("Avatar Press")
        publisher2 = Publisher("  ")
        assert not(publisher1 == publisher2)
        publisher3 = Publisher("Avatar Press")
        assert publisher1 == publisher3

    def test_lt(self):
        publisher1 = Publisher("A")
        publisher2 = Publisher("B")
        assert publisher1 < publisher2






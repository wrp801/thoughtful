import pytest 
from challenge import core 
from challenge.core import Library, Book, Member

def test_question_1():
    assert core.question_1() == [2, 3,4,6,8,9,10,12,14,15,16,18,20]

def test_question_2():
    prices = {'apple': 0.40, 'kiwi': 1.25, 'banana': 0.50}
    assert core.question_2(prices) == [('apple', 0.40), ('banana', 0.50), ('kiwi', 1.25)]

def test_question_3(capsys):
    expected_output = "1\n22\n333\n4444\n55555\n"
    core.question_3(5)
    captured = capsys.readouterr()
    assert captured.out == expected_output


def test_question_4():
    test_numbers = [1, 2, 3, 4]
    test_factor = 2
    core.multiply_by_factor(test_numbers, test_factor)
    assert test_numbers == [2, 4, 6, 8]


def test_question_5():
    assert core.question_5(10, 5) == 2
    assert core.question_5(10, 0) == -1

def test_question_6():
    start = 1 
    end = 20 
    assert core.find_primes(start, end) == [2, 3, 5,7,11,13,17,19]

def test_question_7():
    string = 'racecar'
    assert core.is_palindrome(string) == True
    string = 'hello'
    assert core.is_palindrome(string) == False

def test_question_9():
    people = [
        {"name": "Alice", "age": 25, "citizenship": "Yes"},
        {"name": "Bob", "age": 17, "Visa": "Yes", "Expiration": "2025-01-01"},
        {"name": "Charlie", "age": 20, "citizenship": "No"},
        {"name": "Raul", "age": 18, "citizenship": "Unknown", "state": "MI"},
        {"name": "David", "age": 30, "citizenship": "Yes", "Visa": "Yes", "Expiration": "2023-01-01"},
        {"name": "Eve", "age": 42, "state": "CA", "citizenship": "Yes", "felony_conviction": "Yes"},
    ]
    ans = [ 
        {"name": "Alice", "age": 25, "citizenship": "Yes"},
        {"name": "David", "age": 30, "citizenship": "Yes", "Visa": "Yes", "Expiration": "2023-01-01"},]

    assert core.question_9(people) == ans

def test_question_10():
    assert core.question_10(10) == 55
    assert core.question_10(0) == 0

# Test Book class
def test_book_init():
    book = Book("Title", "Author", "ISBN")
    assert book.title == "Title"
    assert book.author == "Author"
    assert book.isbn == "ISBN"

def test_book_str():
    book = Book("Title", "Author", "ISBN")
    assert str(book) == "Title by Author"

# Test Member class
def test_member_init():
    member = Member("Name", "ID")
    assert member.name == "Name"
    assert member.member_id == "ID"
    assert member.books_checked_out == []

def test_member_check_out_book():
    member = Member("Name", "ID")
    book = Book("Title", "Author", "ISBN")
    member.check_out_book(book)
    assert member.books_checked_out == [book]

def test_member_return_book():
    member = Member("Name", "ID")
    book = Book("Title", "Author", "ISBN")
    member.check_out_book(book)
    member.return_book(book)
    assert member.books_checked_out == []

def test_member_str():
    book1 = Book("Title1", "Author1", "ISBN1")
    book2 = Book("Title2", "Author2", "ISBN2")
    member = Member("Name", "ID")
    member.check_out_book(book1)
    member.check_out_book(book2)
    assert str(member) == "Name (ID: ID) - Title1 by Author1, Title2 by Author2"

# Test Library class
def test_library_init():
    library = Library("Library", [], [])
    assert library.name == "Library"
    assert library.books == []
    assert library.members == []

def test_library_add_book():
    library = Library("Library", [], [])
    book = Book("Title", "Author", "ISBN")
    library.add_book(book)
    assert library.books == [book]

def test_library_add_member():
    library = Library("Library", [], [])
    member = Member("Name", "ID")
    library.add_member(member)
    assert library.members == [member]

def test_library_check_out_book():
    library = Library("Library", [], [])
    member = Member("Name", "ID")
    book = Book("Title", "Author", "ISBN")
    library.add_member(member)
    library.add_book(book)
    library.check_out_book("ID", "ISBN")
    assert member.books_checked_out == [book]
    assert library.books == []


def test_library_str():
    library = Library("Library", [], [])
    assert str(library) == "Library - 0 books, 0 members"

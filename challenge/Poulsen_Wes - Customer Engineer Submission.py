# Customer Engineer Coding Assignment

# Import any libraries you might need to answer the questions below here.
import sys
from collections import Counter
from typing import Optional

## Instructions
    # This quiz consists of ten questions designed to test your knowledge on Python programming. 
    # Please take no more than 2 hours on this quiz.
    # Handle as many edge cases for each question that you can think of. Write unit tests as needed (none are required though).
    # Feel free to use the internet, ChatGPT, or any other resources to help you answer the questions.
    # Please share any resources, or links to chats with an AI that you used to answer the questions.

## Question 1: List Comprehension
    # Write a Python program that uses list comprehension to find all numbers between 1 and 20 that are divisible by 2 or 3.
def question_1():
    # Your code here
    return [x for x in range(1, 21) if x % 2 == 0 or x % 3 == 0]

## Question 2: Working with Dictionaries
    # Given a dictionary, `prices = {'apple': 0.40, 'banana': 0.50, 'kiwi': 1.25}`, write a Python program to convert the prices into a list of `(fruit, price)` tuples, then print the list sorted by fruit name.
def question_2(prices):
    # Your code here
    keys_sorted = sorted(prices.keys())
    return [(key, prices[key]) for key in keys_sorted]

## Question 3: Nested Loops
    # Write a Python program that prints the following pattern using nested loops.

    # For n=5, the pattern should look like this:
#    1
#    22
#    333
#    4444
#    55555

def question_3(n):
    # Your code here
    for i in range(1, n+1):
        print(str(i) * i)

## Question 4: Functions and Namespaces
# Write a function `multiply_by_factor` that takes a list of numbers and a `factor` with which to multiply each number. The function should modify the original list and not return anything.
def multiply_by_factor(num_list, factor):
    # Your code here
    num_list[:] = [num * factor for num in num_list]


## Question 5: Error Handling
# Write a Python program that includes a function divide_numbers which takes two parameters, numerator and denominator. 
# This function should attempt to divide the numerator by the denominator and return the result. 
# However, if the denominator is zero, the function should return -1.
def question_5(numerator, denominator):
    # Your code here
    try:
        return numerator / denominator
    except ZeroDivisionError:
        return -1

## Question 6: Prime Numbers
# Write a Python program to find and print all the prime numbers between two input values, start and end. 
# Use a function named `find_primes` to accomplish this. 
# A prime number is a number that has exactly two distinct positive divisors: 1 and itself.
def find_primes(start, end):
    # Your code here
    def is_prime(n:int):
        if n <= 1:
            return False
        elif n <= 3:
            return True
        elif n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True
    primes = []
    primes = list(filter(is_prime, range(start, end+1)))
    return primes


## Question 7: String Manipulation
# Given a string, write a Python program to check if it is a palindrome. 
# A palindrome is a word, phrase, number, or other sequences of characters that reads the same forward and backward (ignoring spaces, punctuation, and capitalization). 
# Your program should include a function named `is_palindrome` that takes a string as an input and returns `True` if it's a palindrome and `False` otherwise.
def is_palindrome(input_string:str):
    # Your code here
    input_string = input_string.lower()
    return input_string == input_string[::-1]
        

## Question 8: File Processing
# Write a Python program that does the following:
# 1. Reads a text file with it's named passed as an argument to the program. The file contains a list of words separated by spaces.
# 2. Counts the occurrence of each word in the file
# 3. Writes the counts to a new text file, with name also passed as an argument, in the format word: count, one word per line. 
# 4. The words should be sorted in descending order.
def question_8():
    # Your code here
    def count_word_occurrences(input:str, output:str):
        with open(input, 'r') as file:
            words = file.read().split()
        word_count = Counter(words)
        sorted_words = sorted(word_count.items(), key = lambda x: x[1], reverse = True)
        with open(output, 'w') as file:
            for word, count in word_count.most_common():
                file.write(f"{word}: {count}\n")
    input = sys.argv[1]  # grab the input file
    output = sys.argv[2]  # grab the output file
    count_word_occurrences(input, output)

## Question 9: Data Filtering
# Given a list of dictionaries representing different people, write a Python program to filter out those who are not eligible to vote. 
# The criteria for voting eligibility are being at least 18 years old and holding citizenship. 
# Your program should include a function named filter_voters that takes the list of dictionaries and returns a new list containing only the dictionaries of those who are eligible to vote.
# Below is an example list of dictionaries (Note: your program should work for any list of dictionaries with varying structures):
people = [
    {"name": "Alice", "age": 25, "citizenship": "Yes"},
    {"name": "Bob", "age": 17, "Visa": "Yes", "Expiration": "2025-01-01"},
    {"name": "Charlie", "age": 20, "citizenship": "No"},
    {"name": "Raul", "age": 18, "citizenship": "Unknown", "state": "MI"},
    {"name": "David", "age": 30, "citizenship": "Yes", "Visa": "Yes", "Expiration": "2023-01-01"},
    {"name": "Eve", "age": 42, "state": "CA", "citizenship": "Yes", "felony_conviction": "Yes"},
]
def question_9(persons):
    # Your code here
    def filter_voters(person:dict):
        citizenship = person.get("citizenship", "").lower()
        age = person.get("age", 0) # set default to 0
        felony = person.get("felony_conviction", "no").lower() # set default to no
        return age >= 18 and citizenship == "yes" and felony == "no"
    return list(filter(filter_voters, persons))


# Question 10: Recursive Functions
# Write a Python program that implements a recursive function named calculate_fibonacci to find the nth number in the Fibonacci sequence. 
# The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones, usually starting with 0 and 1. 
# Your function should take the term n as an input and return the nth Fibonacci number.
def question_10(n):
    # Your code here
    def calculate_fibonacci(n:int):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        else:
            return calculate_fibonacci(n-1) + calculate_fibonacci(n-2)
    return calculate_fibonacci(n)


## Challenge Question: Object-Oriented Programming - Library Management System
# Write a Python program to implement a simple library management system using object-oriented programming principles. 
# Your program should include classes for Library, Book, and Member. 
# In addition to the instructions below, feel free to add any additional methods or attributes you think are necessary or are needed for your implementation.
# Use the following specifications:

    # Book Class:
    # Attributes: title (str), author (str), isbn (str)
    # Methods: None
    # Other Notes
        # print(Book) should return the title and author of the book as follows: "Book.title by Book.author".


class Book:
    # Your code here
    def __init__(self, title:str, author:str, isbn:str):
        self.title = title
        self.author = author
        self.isbn = isbn

    def __str__(self):
        return f"{self.title} by {self.author}"

    def __eq__(self, other):
        return self.isbn == other.isbn

    # Member Class:
    # Attributes: name (str), member_id (int), books_checked_out (a list of books the member has checked out)
    # Methods:
    # check_out_book(self, book): Adds a book to the member’s books_checked_out list if it's available.
    # return_book(self, book): Removes a book from the books_checked_out list.
    # Other Notes
        # print(Member) should return the member's name, ID, and list of books the member has checked out as follows: "Member.name (ID: Member.member_id) - Member.books_checked_out separated by commas".

class Member:
    # Your code here
    def __init__(self, name:str, member_id:str) -> None:
        self.name = name
        self.member_id = member_id
        self.books_checked_out = []

    def check_out_book(self, book:Book):
        self.books_checked_out.append(book)

    def return_book(self, book:Book):
        if book in self.books_checked_out:
            self.books_checked_out.remove(book)

    def __str__(self):
        books_checked_out_str = ", ".join([str(book) for book in self.books_checked_out])
        return f"{self.name} (ID: {self.member_id}) - {books_checked_out_str}"

    # Library Class:
    # Attributes: name (str), books (a list of all Book objects in the library), members (a list of all Member objects).
    # Methods:
    # add_book(self, book): Adds a new book to the library.
    # add_member(self, member): Adds a new member to the library.
    # check_out_book(self, member_id, isbn): Checks out a book to a member.
    # return_book(self, member_id, isbn): Returns a book from a member.
    # get_member_books(self, member_id): Prints out all books checked out by a member.
    # Other Notes
        # print(Library) should return the library's name and the number of books and members in the library as follows: "Library.name - ### books, ### members".
class Library:
    # Your code here
    def __init__(self, name: str, books: Optional[list[Book]] = None, members: Optional[list[Member]] = None) -> None:
        self.name = name
        self.books = books if books else []
        self.members = members if members else []

    def add_book(self, book: Book):
        self.books.append(book)

    def add_member(self, member: Member):
        self.members.append(member)

    def check_out_book(self, member_id: str, isbn: str):
        member = next((member for member in self.members if member.member_id == member_id), None)
        book = next((book for book in self.books if book.isbn == isbn), None)
        if member and book:
            member.check_out_book(book)
            self.books.remove(book)

    def return_book(self, member_id: str, isbn: str):
        member = next((member for member in self.members if member.member_id == member_id), None)
        book = next((book for book in self.books if book.isbn == isbn), None)
        if member and book:
            member.return_book(book)
            self.books.append(book)

    def get_member_books(self, member_id):
        member = next((member for member in self.members if member.member_id == member_id), None)
        if member:
            print(member.books_checked_out)

    def __str__(self):
        return f"{self.name} - {len(self.books)} books, {len(self.members)} members"




def challenge_question():
    # Your code here
    pass




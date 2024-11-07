import data
from typing import Optional

# Write your functions for each part in the space below.

# Part 0

# Finds the index of the smallest value in the list, if there are values,
#     starting from the provided index (if in bounds).
# input: a list of integers
# input: a starting index
# returns: index of smallest value as an int or None if no value is found
def index_smallest_from(values:list[int], start:int) -> Optional[int]:
    if start >= len(values) or start < 0:
        return None

    mindex = start
    for idx in range(start + 1, len(values)):
        if values[idx] < values[mindex]:
            mindex = idx

    return mindex


# Sorts, in place, the elements of a list using the selection sort algorithm.
# input: a list of integers
# returns: nothing is returned; the list is sorted in place
#    <This function modifies/mutates the input list. Though a traditional
#     approach, cloning the list sorting the clone is potentially less
#     surprising. Or even using a different sorting algorithm.>
def selection_sort(values:list[int]) -> None:
    for idx in range(len(values) - 1):
        mindex = index_smallest_from(values, idx)
        tmp = values[mindex]
        values[mindex] = values[idx]
        values[idx] = tmp


# Part 1
from data import Book
# Finds the index of the smallest title in the list of books, starting from the provided index.
# input: a list of Book objects
# input: a starting index
# returns: index of the book with the smallest title, or None if no value is found
def index_smallest_title(books: list[Book], start: int) -> Optional[int]:
    if start >= len(books) or start < 0:
        return None

    min_index = start
    for idx in range(start + 1, len(books)):
        if books[idx].title < books[min_index].title:
            min_index = idx

    return min_index

# Sorts the list of Book objects by title in alphabetical order.
# input: a list of Book objects
# returns: None; the list is sorted in place by title
def selection_sort_books(books: list[Book]) -> None:
    for idx in range(len(books) - 1):
        min_index = index_smallest_title(books, idx)
        if min_index is not None:
            # Swap the books at idx and min_index
            books[idx], books[min_index] = books[min_index], books[idx]
"""
books = [
    Book(["Neil Gaiman", "Terry Pratchett"], "Good Omens"),
    Book(["Neil Gaiman"], "Neverwhere"),
    Book(["Neil Gaiman"], "American Gods")
]
selection_sort_books(books)
print(books)
"""
# Part 2
def swap_case(input_string: str) -> str:
    result = ""
    for char in input_string:
        if char.isalpha():
            if char.islower():
                result += char.upper()
            else:
                result += char.lower()
        else:
            result += char
    return result
"""
input_string = "hElLo ThErE!"
print(swap_case(input_string))  # Expected output: "HeLlO tHeRe!"
"""

# Part 3
def str_translate(input_str: str, old: str, new: str) -> str:
    result = ""
    for char in input_str:
        if char == old:
            result += new
        else:
            result += char
    return result
"""
input_str = "abcdcba"
old = "a"
new = "x"
print(str_translate(input_str, old, new))  # Expected output: "xbcdcbx"
"""

# Part 4
def histogram(text: str) -> dict[str, int]:
    word_counts = {}
    words = text.split()  # Split text into words based on spaces

    for word in words:
        if word in word_counts:
            word_counts[word] += 1  # Increment count if word is already in dictionary
        else:
            word_counts[word] = 1  # Initialize count to 1 if word is new

    return word_counts
"""
text = "apple banana apple orange banana apple"
print(histogram(text))  # Expected output: {'apple': 3, 'banana': 2, 'orange': 1}
"""

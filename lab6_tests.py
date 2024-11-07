import data
import lab6
import unittest


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 0
    def test_index_smallest_from_1(self):
        input = [2, 1, 9, 0, 4, 5]
        expected = 3
        actual = lab6.index_smallest_from(input, 0)
        self.assertEqual(expected, actual)


    def test_index_smallest_from_2(self):
        input = [2, 1, 9, 0, 4, 5]
        expected = 4
        actual = lab6.index_smallest_from(input, 4)
        self.assertEqual(expected, actual)


    def test_index_smallest_from_3(self):
        input = [2, 1, 9, 0, 4, 5]
        expected = None
        actual = lab6.index_smallest_from(input, 6)
        self.assertEqual(expected, actual)


    def test_index_smallest_from_4(self):
        input = []
        expected = None
        actual = lab6.index_smallest_from(input, 0)
        self.assertEqual(expected, actual)


    def test_selection_sort_1(self):
        input = [1, 2, 3, 4, 5]
        expected = [1, 2, 3, 4, 5]
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    def test_selection_sort_2(self):
        input = []
        expected = []
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    def test_selection_sort_3(self):
        input = [9, 7, 5, 3, 1]
        expected = [1, 3, 5, 7, 9]
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    def test_selection_sort_4(self):
        input = [5, 0, 19, 21, 4, 6]
        expected = [0, 4, 5, 6, 19, 21]
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    # Part 1

    from data import Book
    import lab6

    class TestSelectionSortBooks(unittest.TestCase):
        def test_selection_sort_books_empty(self):
            books = []
            expected = []
            lab6.selection_sort_books(books)
            self.assertEqual(books, expected)

        def test_selection_sort_books_single(self):
            books = [Book(["Neil Gaiman"], "American Gods")]
            expected = [Book(["Neil Gaiman"], "American Gods")]
            lab6.selection_sort_books(books)
            self.assertEqual(books, expected)

        def test_selection_sort_books_multiple(self):
            books = [
                Book(["Neil Gaiman", "Terry Pratchett"], "Good Omens"),
                Book(["Neil Gaiman"], "Neverwhere"),
                Book(["Neil Gaiman"], "American Gods")
            ]
            expected = [
                Book(["Neil Gaiman"], "American Gods"),
                Book(["Neil Gaiman", "Terry Pratchett"], "Good Omens"),
                Book(["Neil Gaiman"], "Neverwhere")
            ]
            lab6.selection_sort_books(books)
            self.assertEqual(books, expected)

    # Part 2
    from lab6 import swap_case

    def test_swap_case_empty_string(self):
        self.assertEqual("", lab6.swap_case(""))

    def test_swap_case_all_lowercase(self):
        self.assertEqual("HELLO WORLD", lab6.swap_case("hello world"))

    def test_swap_case_all_uppercase(self):
        self.assertEqual("hello world", lab6.swap_case("HELLO WORLD"))


    def test_swap_case_mixed_case(self):
        self.assertEqual("hELLO wORLD", lab6.swap_case("Hello World"))

    def test_swap_case_non_english_letters(self):
        self.assertEqual("ÜbeR sCHÖN", lab6.swap_case("üBEr Schön"))

    # Part 3
    def test_str_translate_basic(self):
        input_str = "abcdcba"
        old = "a"
        new = "x"
        expected = "xbcdcbx"
        actual = lab6.str_translate(input_str, old, new)
        self.assertEqual(actual, expected)

    def test_str_translate_no_replacements(self):
        input_str = "hello world"
        old = "z"
        new = "x"
        expected = "hello world"  # No 'z' in the string, so no replacements
        actual = lab6.str_translate(input_str, old, new)
        self.assertEqual(actual, expected)

    def test_str_translate_all_replacements(self):
        input_str = "aaaaa"
        old = "a"
        new = "b"
        expected = "bbbbb"  # All 'a's are replaced with 'b's
        actual = lab6.str_translate(input_str, old, new)
        self.assertEqual(actual, expected)

    # Part 4
    def test_histogram_basic(self):
        text = "apple banana apple orange banana apple"
        expected = {"apple": 3, "banana": 2, "orange": 1}
        actual = lab6.histogram(text)
        self.assertEqual(actual, expected)

    def test_histogram_single_word(self):
        text = "grape grape grape"
        expected = {"grape": 3}
        actual = lab6.histogram(text)
        self.assertEqual(actual, expected)

    def test_histogram_empty_string(self):
        text = ""
        expected = {}
        actual = lab6.histogram(text)
        self.assertEqual(actual, expected)




if __name__ == '__main__':
    unittest.main()

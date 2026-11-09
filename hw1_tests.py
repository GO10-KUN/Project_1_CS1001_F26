"""CSC 1001 - Programming Assignment 1: student-written unit tests.

Create at least TWO separate, meaningful unit tests for each function.
The sixteen methods below are ONLY PLACEHOLDERS: they are not real tests.

Replace each self.fail(...) with test inputs, a call to the appropriate
hw1 function, and unittest assertions about its expected output.
Use methods like self.assertEqual(...) or self.assertAlmostEqual(...).

IMPORTANT: The initial test failures are intentional until you write tests
and implement the functions in hw1.py. Do not simply delete the tests.
"""

import unittest

import data
import hw1


class TestHomework1(unittest.TestCase):

    # Part 1: vowel_count
    def test_vowel_count_case_insensitive(self):
        self.assertEqual(hw1.vowel_count("HEllO World"), 3)

    def test_vowel_count_empty_string(self):
        self.assertEqual(hw1.vowel_count(""), 0)

    # Part 2: short_lists
    def test_short_lists_mixed_lengths(self):
        self.assertEqual(hw1.short_lists([[1, 2], [3], [4, 5, 6], [7, 8]]), [[1, 2], [7, 8]])

    def test_short_lists_no_matching_lengths(self):
        self.assertEqual(hw1.short_lists([[1], [2], [3]]), [])

    # Part 3: ascending_pairs
    def test_ascending_pairs_reversed_pairs(self):
        self.assertEqual(hw1.ascending_pairs([[2, 1], [5, 4]]), [[1, 2], [4, 5]])

    def test_ascending_pairs_other_lengths_unchanged(self):
        self.assertEqual(hw1.ascending_pairs([[3, 2, 1], [4, 5]]), [[3, 2, 1], [4, 5]])

    # Part 4: add_prices
    def test_add_prices_no_cents_carry(self):
        first = data.Price(1, 50)
        second = data.Price(2, 30)
        expected = data.Price(3, 80)
        self.assertEqual(hw1.add_prices(first, second), expected)

    def test_add_prices_with_cents_carry(self):
        first = data.Price(1, 80)
        second = data.Price(2, 75)
        expected = data.Price(4, 55)
        self.assertEqual(hw1.add_prices(first, second), expected)

    # Part 5: rectangle_area
    def test_rectangle_area_standard_rectangle(self):
        # TODO: Arrange inputs, call hw1.rectangle_area, and assert the result.
        self.assertEqual(hw1.rectangle_area(data.Rectangle(data.Point(0, 0), data.Point(4, 3))), 12)

    def test_rectangle_area_negative_coordinates(self):
        # TODO: Arrange inputs, call hw1.rectangle_area, and assert the result.
        self.assertEqual(hw1.rectangle_area(data.Rectangle(data.Point(-2, -1), data.Point(2, 2))), 12)

    # Part 6: books_by_author
    def test_books_by_author_matching_authors(self):
        # TODO: Arrange inputs, call hw1.books_by_author, and assert the result.
        self.assertEqual(hw1.books_by_author("Author A", [data.Book("Author A", "Book 1"), data.Book("Author B", "Book 2")]), [data.Book("Author A", "Book 1")])

    def test_books_by_author_no_matches(self):
        # TODO: Arrange inputs, call hw1.books_by_author, and assert the result.
        self.assertEqual(hw1.books_by_author("Author C", [data.Book("Author A", "Book 1"), data.Book("Author B", "Book 2")]), [])
    
    # Part 7: circle_bound
    def test_circle_bound_square(self):
        # TODO: Arrange inputs, call hw1.circle_bound, and assert the result.
        self.fail("TODO: write the first unit test for circle_bound")

    def test_circle_bound_non_square_rectangle(self):
        # TODO: Arrange inputs, call hw1.circle_bound, and assert the result.
        self.fail("TODO: write the second unit test for circle_bound")

    # Part 8: below_pay_average
    def test_below_pay_average_different_pay_rates(self):
        # TODO: Arrange inputs, call hw1.below_pay_average, and assert the result.
        self.fail("TODO: write the first unit test for below_pay_average")

    def test_below_pay_average_empty_list(self):
        # TODO: Arrange inputs, call hw1.below_pay_average, and assert the result.
        self.fail("TODO: write the second unit test for below_pay_average")


if __name__ == '__main__':
    unittest.main()

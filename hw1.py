"""CSC 1001 - Programming Assignment 1.

Student starter file. Implement the eight required functions below.
The provided data types live in data.py; do not edit data.py.

For EVERY function, replace the TODO documentation with a short comment
explaining its purpose, input(s), and output. You may write helper functions.
"""

import data


# Part 1: vowel_count
def vowel_count(text: str) -> int:
    # TODO: Purpose: Goes through the given string and counts the number of vowels in it.
    # TODO: Input(s): text (str) - the string to analyze.
    # TODO: Output: int - the number of vowels in the string.
    count = 0
    vowels = {'a', 'e', 'i', 'o', 'u'}
    for char in text:
        if char.lower() in vowels:
            count += 1
    return count


# Part 2: short_lists
def short_lists(items: list[list[int]]) -> list[list[int]]:
    # TODO: Purpose: Goes through a list of lists and returns those with exactly two elements.
    # TODO: Input(s): The list of lists to analyze.
    # TODO: Output: The list of lists with exactly two elements.
    result = []
    for item in items:
        if len(item) == 2:
            result.append(item)
    return result


# Part 3: ascending_pairs
def ascending_pairs(items: list[list[int]]) -> list[list[int]]:
    # TODO: Purpose: Returns a new list of lists where lists with a length of 2 are sorted in ascending 
    #                order, while other lists remain unchanged.
    # TODO: Input(s): items (list of lists of int) - the list of lists to analyze.
    # TODO: Output: list[list[int]] - the new list of lists with ascending pairs.
    result = []
    for item in items:
        if len(item) == 2:
            result.append(sorted(item))
        else:
            result.append(item)
    return result


# Part 4: add_prices
def add_prices(first: data.Price, second: data.Price) -> data.Price:
    # TODO: Purpose: Adds two Price objects together and returns a new Price object representing the total.
    #                Adds the dollars and cents separately, carrying over if cents exceed 100.
    # TODO: Input(s): Two Price objects to add together.
    # TODO: Output: The sum of the two Price objects as a new Price object.
    result = data.Price(first.dollars + second.dollars, first.cents + second.cents)
    if result.cents >= 100:
        result.dollars += result.cents // 100
        result.cents = result.cents % 100
    return result


# Part 5: rectangle_area
def rectangle_area(rectangle: data.Rectangle) -> float:
    # TODO: Purpose: Calculates the area of a given rectangle using its width and height.
    # TODO: Input(s): Rectangle object for which to calculate the area.
    # TODO: Output: The area of the rectangle as a float.
    width = rectangle.top_left.x - rectangle.bottom_right.x
    height = rectangle.top_left.y - rectangle.bottom_right.y
    return width * height


# Part 6: books_by_author
def books_by_author(author: str, books: list[data.Book]) -> list[data.Book]:
    # TODO: Purpose: Returns a list of books written by the specified author from a given list of Book objects.
    # TODO: Input(s): author (str) - the name of the author to search for.
    #                 books (list[data.Book]) - the list of Book objects to search through.
    # TODO: Output: A list of Book objects written by the specified author.
    result = []
    for book in books:
        if book.authors == author:
            result.append(book)
    return result


# Part 7: circle_bound
def circle_bound(rectangle: data.Rectangle) -> data.Circle:
    # TODO: Purpose: Returns a Circle object that encloses the given rectangle,
    #                with the circle's center at the rectangle's center and
    #                radius equal any of the rectangle's corners.
    # TODO: Input(s): rectangle (data.Rectangle) - the rectangle to enclose in a circle.
    #                 The rectangle is defined by its top-left and bottom-right corners.
    # TODO: Output: The Circle object that surrounds the rectangle, with the center at the rectangle's
    #               center and radius equal to the distance from the center to any corner of the rectangle.
    center_x = (rectangle.top_left.x + rectangle.bottom_right.x) / 2
    center_y = (rectangle.top_left.y + rectangle.bottom_right.y) / 2
    radius = ((rectangle.top_left.x - center_x) ** 2 + (rectangle.top_left.y - center_y) ** 2) ** 0.5
    return data.Circle(data.Point(center_x, center_y), radius)


# Part 8: below_pay_average
def below_pay_average(employees: list[data.Employee]) -> list[str]:
    # TODO: Purpose: describe what this function computes.
    # TODO: Input(s): explain each parameter.
    # TODO: Output: explain what the function returns.
    # TODO: Replace this exception with your implementation.
    raise NotImplementedError("Part 8: implement below_pay_average")

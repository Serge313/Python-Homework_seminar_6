"""Задача 32: Определить индексы элементов массива (списка), значения
которых принадлежат заданному диапазону (т.е. не меньше заданного
минимума и не больше заданного максимума)"""


import sys


class MaxMinError(Exception):
    pass


def fill_list_of_numbers(list, n):
    """The method fills empty list"""
    count = 1
    while count <= n:
        try:
            number = int(input(f"Enter the number at index {count - 1}: "))
        except ValueError as exc:
            print(f"Error: {exc}")
            sys.exit()
        list.append(number)
        count += 1
    return list


def find_indexes_in_range(list, minimum, maximum):
    """The method finds the indexes of whose values belong to the given range"""
    list_of_i = []
    for i in range(len(list)):
        if minimum <= list[i] <= maximum:
            list_of_i.append(i)
    return list_of_i


def testing_find_indexes_in_range(test_list=[1, 2, 3, 4, 5, 6, 7, 8], test_min=3, test_max=7):
    """The method tests find_indexes_in_range method"""
    print("Testing of the \"find_indexes_in_range\" method has been launched...")
    expected = [2, 3, 4, 5, 6]
    actual = find_indexes_in_range(test_list, test_min, test_max)
    is_equal = expected == actual
    if is_equal:
        print("Test completed successfully!")
    else:
        print("Error! Need to fix the method!")
        print(actual)


testing_find_indexes_in_range()
print()


try:
    number_of_elements = int(input("Enter the number of elements: "))
except ValueError as e:
    print(f"Error: {e}")
    sys.exit()


try:
    min_value = int(input("Enter the minimum value: "))
except ValueError as e:
    print(f"Error: {e}")
    sys.exit()


try:
    max_value = int(input("Enter the maximum value: "))
    if max_value < min_value:
        raise MaxMinError("Invalid maximum or minimum value entered!")
except ValueError as e:
    print(f"Error: {e}")
    sys.exit()
except MaxMinError as ex:
    print(ex)
    sys.exit()


print()
empty_list = []
list_of_numbers = fill_list_of_numbers(empty_list, number_of_elements)
print()
list_of_indexes = find_indexes_in_range(list_of_numbers, min_value, max_value)
print(f"The indexes of whose values belong to the given range: {list_of_indexes}")

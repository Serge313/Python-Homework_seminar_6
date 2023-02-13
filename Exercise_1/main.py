"""Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент,
разность и количество элементов нужно ввести с клавиатуры.
Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
Каждое число вводится с новой строки."""


import sys


def fill_list_of_progression(list, first_el, diff, num_of_el):
    """The method fills list with elements of an arithmetical progression"""
    for i in range(1, num_of_el + 1):
        list.append(first_el + (i - 1) * diff)
    return list


def testing_fill_list_of_progression(test_list=[], test_first_el=2, test_diff=2, test_num_of_el=8):
    """The method tests fill_list_of_progression method"""
    print("Testing of the \"fill_list_of_progression\" method has been launched...")
    expected = [2, 4, 6, 8, 10, 12, 14, 16]
    actual = fill_list_of_progression(test_list, test_first_el, test_diff, test_num_of_el)
    is_equal = expected == actual
    if is_equal:
        print("Test completed successfully!")
    else:
        print("Error! Need to fix the method!")


testing_fill_list_of_progression()
print()


try:
    first_element = int(input("Enter the first element of the progression: "))
except ValueError as e:
    print(f"Error: {e}")
    sys.exit()


try:
    difference = int(input("Enter the difference of the progression: "))
except ValueError as e:
    print(f"Error: {e}")
    sys.exit()


try:
    number_of_elements = int(input("Enter the number of elements of the progression: "))
except ValueError as e:
    print(f"Error: {e}")
    sys.exit()


print()
empty_list = []
progression = fill_list_of_progression(empty_list, first_element, difference, number_of_elements)
print(f"Your arithmetical progression: {progression}")

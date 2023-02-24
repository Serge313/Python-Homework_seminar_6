"""Доп задача:
Два различных натуральных числа n и m называются дружественными,
если сумма делителей числа n (включая 1, но исключая само n)
равна числу m и наоборот. Например, 220 и 284 – дружественные числа.
По данному числу k выведите все пары дружественных чисел, каждое
из которых не превосходит k. Программа получает на вход одно
натуральное число k, не превосходящее 10^5. Программа должна
вывести  все пары дружественных чисел, каждое из которых не
превосходит k. Пары необходимо выводить по одной в строке,
разделяя пробелами. Каждая пара должна быть выведена только
один раз (перестановка чисел новую пару не дает)."""


def find_divisors_sum(num):
    """The method finds the sum of divisors"""
    divisors_sum = 0
    for i in range(1, num):
        if num % i == 0:
            divisors_sum += i
    return divisors_sum


def find_friendly_numbers(k):
    """The method finds all pairs of friendly numbers"""
    friendly_pairs = []
    for i in range(1, k+1):
        div_sum_i = find_divisors_sum(i)
        for j in range(i+1, k+1):
            if div_sum_i == j and find_divisors_sum(j) == i:
                friendly_pairs.append((i, j))
    return friendly_pairs


k = int(input("Enter number \"k\" "))
friendly_pairs = find_friendly_numbers(k)


for pair in friendly_pairs:
    print(pair[0], pair[1])

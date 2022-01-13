"""
Домашнее задание №1
Функции и структуры данных
"""
import math


def square(number):
    return number ** 2


def power_numbers(*args):
    #     """
    #         функция, которая принимает N целых чисел,
    #         и возвращает список квадратов этих чисел
    #         >>> power_numbers(1, 2, 5, 7)
    #         <<< [1, 4, 25, 49]
    #         """
    outlist = list(map(square, args))
    return outlist


ODD = "odd"
EVEN = "even"
PRIME = "prime"


def filter_odd(in_num):
    return (in_num % 2) == 1


def filter_even(in_num):
    return (in_num % 2) == 0


def is_prime(num):
    if num < 2:
        return False
    else:
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return False
        return True


def filter_numbers(numbers, const):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)
    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """

    if const == ODD:
        out_filter = filter(filter_odd, numbers)
        return list(out_filter)

    if const == EVEN:
        out_filter = filter(filter_even, numbers)
        return list(out_filter)

    if const == PRIME:
        out_filter = filter(is_prime, numbers)
        return list(out_filter)

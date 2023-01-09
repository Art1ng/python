"""
Домашнее задание №1
Функции и структуры данных
"""
def power_numbers(*args):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    """
    return [x ** 2 for x in args]

# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def is_prime(n):
   if n <= 1 or n % 1 > 0:
      return False
   for i in range(2, n):
      if n % i == 0:
         return False
   return True


FILTERS_MAP = {
    ODD: lambda n: n % 2 != 0,
    EVEN: lambda n: n % 2 == 0,
    PRIME: is_prime,
}


def filter_numbers(list_of_numbers, type_of_number):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)
    """
    return list(filter(FILTERS_MAP[type_of_number], list_of_numbers))

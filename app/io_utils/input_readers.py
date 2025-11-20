"""Модуль функций ввода данных.
Содержит безопасное чтение двух целых чисел a и b.
"""

def read_int_pair(prompt_a: str = 'Введите a (целое): ',
                   prompt_b: str = 'Введите b (целое, >= a): '):
    """Считывает два целых числа a и b.
    Если ввод некорректен — вызывается исключение.

    :param prompt_a: текст подсказки для первого числа
    :param prompt_b: текст подсказки для второго числа
    :return: кортеж (a, b)
    """
    try:
        a = int(input(prompt_a))
        b = int(input(prompt_b))
    except ValueError:
        raise ValueError('Ошибка: введено не целое число.')

    return a, b

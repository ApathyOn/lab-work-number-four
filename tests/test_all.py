import string
import pytest

from app.generators.abs_range import abs_range
from app.generators.password_generator import password_generator
from app.generators.pairwise_products import pairwise_products


# ------------------------------
# ЗАДАНИЕ 1 — abs_range
# ------------------------------
def test_abs_range_basic():
    gen = abs_range(-3, 2)
    result = [next(gen) for _ in range(6)]
    assert result == [3, 2, 1, 0, 1, 2]


def test_abs_range_single_value():
    gen = abs_range(5, 5)
    assert next(gen) == 5


def test_abs_range_order_independent():
    # если студент перепутает a и b — генератор должен работать корректно
    gen = abs_range(2, -2)
    result = [next(gen) for _ in range(5)]
    assert result == [2, 1, 0, 1, 2]


# ------------------------------
# ЗАДАНИЕ 2 — password_generator
# ------------------------------
def test_password_length_and_charset():
    chars = string.ascii_lowercase + string.ascii_uppercase + "0123456789!?@#$*"
    gen = password_generator(chars)

    pwd = next(gen)

    assert len(pwd) == 12
    assert all(c in chars for c in pwd)


def test_password_uniqueness():
    chars = string.ascii_lowercase + string.ascii_uppercase + "0123456789!?@#$*"
    gen = password_generator(chars)

    passwords = {next(gen) for _ in range(5)}

    # хотя бы 2 разных пароля
    assert len(passwords) >= 2


# ------------------------------
# ЗАДАНИЕ 3 — pairwise_products
# ------------------------------
def test_pairwise_basic():
    gen = pairwise_products([2, 3, 4], [5, 6, 7])
    assert next(gen) == 10
    assert next(gen) == 18
    assert next(gen) == 28


def test_pairwise_negative():
    gen = pairwise_products([-2, 3], [4, -5])
    assert next(gen) == -8
    assert next(gen) == -15


def test_pairwise_ignores_extra_elements():
    # Лишний элемент второго списка должен игнорироваться
    gen = pairwise_products([1, 2, 3, 4], [10, 20, 30])
    assert next(gen) == 10    # 1*10
    assert next(gen) == 40    # 2*20
    assert next(gen) == 90    # 3*30
def abs_range(a: int, b: int):
    """Генератор модулей чисел от min(a,b) до max(a,b) включительно."""
    start, end = min(a, b), max(a, b)
    for i in range(start, end + 1):
        yield abs(i)
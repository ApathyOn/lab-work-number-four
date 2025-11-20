def pairwise_products(list1, list2):
    """Генератор попарных произведений двух списков."""
    return map(lambda x: x[0] * x[1], zip(list1, list2))
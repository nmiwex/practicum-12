def count(a: int, b: int):
    if a > b:
        return count(b, a)
    if a == b:
        return 0

    return count(a, b - a) + 1
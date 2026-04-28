def degree5(n: int):
    if n == 1:
        return 0
    if n % 5 != 0:
        return -1
    result = degree5(n // 5)
    if result == -1:
        return -1
    return result + 1

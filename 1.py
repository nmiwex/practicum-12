def pownum(a: float, n: int):
    if n == 0:
        return 1
    return a * pownum(a, n - 1)


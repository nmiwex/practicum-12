def sum_progress(a1, r, n):
    if n == 0:
        return 0
    if n == 1:
        return a1
    return a1 + sum_progress(a1 + r, r, n - 1)
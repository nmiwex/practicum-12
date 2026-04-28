def maxlist(a: list):
    if len(a) == 1:
        return a[0]

    max_el = maxlist(a[1:])
    return a[0] if a[0] > max_el else max_el

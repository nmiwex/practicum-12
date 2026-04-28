def odd_list(a: list, n: int):
    if n == 0:
        return []
    odd_numbers = odd_list(a, n - 1)

    if a[n - 1] % 2 ==0:
        odd_numbers.append(a[n - 1])
    return odd_numbers
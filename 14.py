def numbers(x: int):
    print(x % 10)

    if x < 10:
        return x
    return numbers(x // 10)

numbers(1234)
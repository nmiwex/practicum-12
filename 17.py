def function1(x: int):
    if x <= 1:
        return 0


    def helper(divisor):
        if divisor * divisor > x:
            return 1
        if x % divisor == 0:
            return 0
        return helper(divisor + 1)


    return helper(2)

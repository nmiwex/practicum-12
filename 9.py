def combin(n, k):
    if k == 0:
        return 1
    result = n / k
    return combin(n - 1, k - 1) * result
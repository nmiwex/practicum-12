def ind_maxlist(a: list):
    if len(a) == 1:
        return 0

    max_ind = ind_maxlist(a[1:])
    return 0 if a[0] >= a[max_ind + 1] else max_ind + 1
def binary_search(val, tab) -> int:
    length = len(tab) - 1
    start = idx = 0
    while start <= length:
        idx = (start + length)//2
        if tab[idx] > val:
            length = idx - 1
        elif tab[idx] < val:
            start = idx + 1
        elif tab[idx] == val:
            start = length + 1
    while idx > 0 and tab[idx - 1] == val:
        idx -= 1
    return idx if tab[idx] == val else -1

def sum_of_two_elements(suma, tab) -> (int, int):
    a = 0
    b = len(tab)-1
    while a < b:
        if tab[a] + tab[b] > suma:
            b -= 1
        elif tab[a] + tab[b] < suma:
            a += 1
        else:
            return a, b
    return -1, -1

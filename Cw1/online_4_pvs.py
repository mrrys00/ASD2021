def min_max_alt(tab):
    length = len(tab)
    minimum = maximum = i = 0
    if length % 2 == 0:
        i = 2
        if tab[0] > tab[1]:
            minimum = tab[1]
            maximum = tab[0]
        else:
            minimum = tab[0]
            maximum = tab[1]
    else:
        i = 1
        minimum = tab[0]
        maximum = tab[0]

    while i < length-1:
        if tab[i] < tab[i+1]:
            minimum = min(minimum, tab[i])
            maximum = max(maximum, tab[i+1])
        else:
            minimum = min(minimum, tab[i+1])
            maximum = max(maximum, tab[i])
        i += 2
    return minimum, maximum

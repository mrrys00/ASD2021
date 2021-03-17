tab = [5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 5, 5, 5, 3, 6,
       6, 6, 6, 5, 6, 6, 7, 8, 5, 5, 4, 5, 6, 6, 6, 6, 5, 6, 6, 5]


def lider(tab) -> int:
    length = len(tab)
    lider = tab[0]
    do_skreslenia = 1  # wykreśla parami różne liczby
    for i in range(1, length):
        if do_skreslenia == 0:
            lider = tab[i]
            do_skreslenia = 1
        elif lider == tab[i]:
            do_skreslenia += 1
        else:
            do_skreslenia -= 1

    if do_skreslenia == 0:
        return None

    wystapienia = 0
    for i in range(length):
        if tab[i] == lider:
            wystapienia += 1
    return lider if wystapienia > length//2 else None


# print(lider(tab))

def zlicz_inwersje(T, l, r) -> int:
    if l >= r-1:
        return 0
    mid = (l + r)//2
    result = zlicz_inwersje(T, l, mid) + zlicz_inwersje(T, mid, r)
    tab = T[l:mid]
    i = 0  # Przechodzi po lewej stronie (tablicy pomocniczej)
    j = mid  # Przechodzi po prawej stronie (nieskopiowanej)
    mid = mid - l  # wyznacza długość tablicy pomocniczej
    while i < mid and j < r:  # Scalanie
        if tab[i] <= T[j]:
            T[l] = tab[i]
            i += 1
        else:
            T[l] = T[j]
            j += 1
            result += mid - i
        l += 1
    if i < mid:  # Jeśli pozostały elementy w tablicy pomocniczej
        T[l:r] = tab[i:mid]  # Kopiujemy je do oryginalnej tablicy
    return result

# Wywołanie:
# t1 = [2, 4, 1, 3, 5] ma 3 inwersje
# print( zlicz_inwersje(t1, 0, len(t1)) )

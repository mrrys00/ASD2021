# Sortowanie tablicy przez scalanie serii naturalnych
# Bottom-up / Z dołu do góry
def merge(T, l, mid, r):
    tab = [T[i] for i in range(l, mid)]
    i = 0  # Przechodzi po lewej stronie (tablicy pomocniczej)
    j = mid  # Przechodzi po prawej stronie (nieskopiowanej)
    mid = j - l  # wyznacza długość tablicy pomocniczej
    while i < mid and j < r:  # Scalanie
        if tab[i] <= T[j]:
            T[l] = tab[i]
            i += 1
        else:
            T[l] = T[j]
            j += 1
        l += 1
    while i < mid:  # Jeśli pozostały elementy w tablicy pomocniczej
        T[l] = tab[i]  # Kopiujemy je do oryginalnej tablicy
        i += 1
        l += 1
    return T


def series(T, l):
    while l < len(T)-1:
        if T[l] > T[l+1]:
            return l
        l += 1
    return l


def natural_merge_sort(T, length):
    m = 1
    while m < length:
        i = l = mid = r = 0
        while i < length:
            l = i
            mid = series(T, i) + 1
            i = mid
            r = series(T, i) + 1
            i = r
            if mid < length:
                merge(T, l, mid, r)
        m = r - l


# Wywołanie:
# natural_merge_sort(first)

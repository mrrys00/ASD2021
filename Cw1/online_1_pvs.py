def bubble_sort(T):
    # Sortowanie bąbelkowe
    length = len(T)
    for i in range(length):
        for j in range(length-i-1):
            if T[j] > T[j+1]:
                T[j], T[j+1] = T[j+1], T[j]
    return T


def insert_sort(T):
    # Sortowanie przez wstawianie
    length = len(T)
    for i in range(1, length):
        j = i-1
        while j >= 0 and T[j] > T[j+1]:
            T[j], T[j+1] = T[j+1], T[j]
            j -= 1
    return T


def selection_sort(T):
    # Sortowanie przez wybieranie
    length = len(T)
    for i in range(0, length):
        m = i
        for j in range(i+1, length):
            if T[j] < T[m]:
                m = j
        T[i], T[m] = T[m], T[i]
    return T

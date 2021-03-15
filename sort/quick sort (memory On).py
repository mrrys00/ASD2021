def quickSort(table, low = 0, high = -1):
    if high == -1: high = len(table) - 1
    while low < high:
        pivot = tablePart(table, low, high)
        if pivot - low < high - pivot:
            quickSort(table, low, pivot - 1)
            low = pivot + 1
        else:
            quickSort(table, pivot + 1, high)
            high = pivot - 1
    return table

def tablePart(table, low, high):
    pivot, i = table[high], low                         # pivot to ostatni element, i = low bo zaczynamy od początku tabeli
    for j in range(low, high):                          # loop od początku do końca tabeli
        if table[j] < pivot:                            # jeżeli element jest mniejszy od piwota to:
            table[i], table[j] = table[j], table[i]     #     swap
            i += 1                                      # zwiększamy i, po koleji ustawiając elementy mniejsze od piwota po lewej, a większe od piwot przesuwane są w prawo
    table[i], table[high] = table[high], table[i]       # ostatni element zamieniamy z elementem [i]. pivot znajduje się pomiędzy elementami mniejszymi od siebie i większymi
    return i

table = [5, 40, 2, 1, 30]
print (table), print (quickSort(table))
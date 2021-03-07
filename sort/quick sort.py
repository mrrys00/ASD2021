def quickSort(table, low = 0, high = -1):
    if high == -1: high = len(table) - 1
    if low < high:
        pivot = tablePart(table, low, high)
        quickSort(table, low, pivot - 1)
        quickSort(table, pivot + 1, high)
    return table

def tablePart(table, low, high):
    pivot, i = table[high], low
    for j in range(low, high):
        if table[j] < pivot:
            table[i], table[j] = table[j], table[i]
            i += 1
    table[i], table[high] = table[high], table[i]
    return i

table = [5, 4, 2, 1, 3]
print (table), print (quickSort(table))
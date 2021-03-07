def selectionSort(table):
    if len(table) < 2: return table
    for i in range(len(table)):
        j = table.index (min(table [i:]))
        table [i], table [j] = table [j], table [i]
    return table

table = [5, 4, 2, 1, 3]
print (table), print (selectionSort(table))
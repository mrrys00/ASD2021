def mergeSort(table):
  if len(table) > 1:
    middle = len(table) // 2
    left = mergeSort(table[:middle])
    right = mergeSort(table[middle:])
    l = r = t = 0
    while l < len(left) and r < len(right):
      if left[l] < right[r]:
        table[t] = left [l]
        l, t = l + 1, t + 1
      else:
        table[t] = right [r]
        r, t= r + 1, t + 1
    while l < len (left):
      table [t] = left [l]
      l, t = l + 1, t + 1
    while r < len (right):
      table [t] = right [r]
      r, t= r + 1, t + 1
  return table

table = [5, 4, 2, 1, 3]
print (table), print (mergeSort(table))
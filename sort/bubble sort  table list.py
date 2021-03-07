class Node:
    def __init__(self, value = None, next = None):
        self.value = value
        self.next = next
    def __str__(self):
        return str(self.value) + " -> " + str(self.next)

def tableToList(table):
    root = Node("!", None) # warden
    current = root
    for i in table:
        current.next = Node(i, None)
        current = current.next
    return root

def tableBubbleSort(table):
    if len(table) < 2: return table
    for i in range(len(table)):
        for j in range(len(table) - i - 1):
            if table [j] > table [j+1]: table [j], table [j+1] = table [j+1], table [j]
    return table

def listBubbleSort(path):
    if path == None or path.next == None or path.next.next == None: return path
    # sprawdza czy puste, tylko warden, tylko waren i 1 liczba
    notSorted = True
    left = path.next
    while left != None:
        right = left.next
        while right != None:
            if left.value > right.value:
                left.value, right.value = right.value, left.value
            right = right.next
        left = left.next
    return path

table = [5, 4, 2, 1, 3]
path = tableToList(table)
print (table), print (tableBubbleSort(table))
print (path), print (listBubbleSort(path))
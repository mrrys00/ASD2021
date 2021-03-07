class Node():
    def __init__(self):
        self.val = None
        self.nxt = None

def insert_value(n, first):
    # podpunkt 2
    if first.val > n:
        prev = Node()
        prev.val = n
        prev.nxt = first
        first = prev
        return first

    prev = first
    temp = first.nxt

    while temp != None:
        if temp.val < n:
            prev = temp
            temp = temp.nxt
        else:
            prev.nxt = Node()
            prev.nxt.val = n
            prev.nxt.nxt = temp
            return first
    prev.nxt = Node()
    prev.nxt.val = n
    return first


def delete_max_with_multiple_occurrences(first: Node):
    # podpunkt 3
    if first == None:
        return first
    temp = first.nxt
    maximum = first.val
    n = 1
    while temp != None:
        if temp.val > maximum:
            maximum = temp.val
            n = 1
        elif temp.val == maximum:
            n += 1
        temp = temp.nxt
    temp = Node()
    temp.nxt = first
    first = temp
    while n > 0 and temp.nxt != None:
        if first.nxt.val == maximum:
            first.nxt = first.nxt.nxt
            n -= 1
        else:
            first = first.nxt
    return temp.nxt


def insert_sort(first):
    # podpunkt 3
    # To nie jest do końca zgodne z poleceniem zadania 2,
    # bo nie używam powyższych funkcji
    if first.nxt == None:
        return first
        
    p = first.nxt
    prev = first

    while p != None:
        if prev.val <= p.val:
            prev = p
            p = p.nxt
        elif p.val <= first.val:
            prev.nxt = p.nxt
            p.nxt = first
            first = p
            p = prev.nxt
        else:
            prev.nxt = p.nxt
            temp = first
            while p!=temp:
                if p.val < temp.nxt.val:
                    p.nxt = temp.nxt
                    temp.nxt = p
                temp = temp.nxt
            p = prev.nxt
    return first

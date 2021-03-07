def list_reverse(first):
    prev = first
    temp = first.nxt
    prev.nxt = None
    while temp != None:
        first = temp
        temp = temp.nxt
        first.nxt = prev
        prev = first
    return first

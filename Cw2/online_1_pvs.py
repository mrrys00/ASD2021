class Node():
    def __init__(self):
        self.val = None
        self.nxt = None


# Podpunkt 1: Scalanie 2 list posortowanych
def merge_sorted_lists(first: Node, second: Node) -> Node:
    final = None
    if first.val > second.val:
        final = second
        second = second.nxt
    else:
        final = first
        first = first.nxt
    result = final
    while first != None and second != None:
        if first.val > second.val:
            final.nxt = second
            second = second.nxt
        else:
            final.nxt = first
            first = first.nxt
        final = final.nxt

    if first != None:
        final.nxt = first
    else:
        final.nxt = second
    return result


# Podpunkt 2: Natural Merge Sort - Sortowanie przez scalanie naturalne
# https://pl.wikipedia.org/wiki/Sortowanie_przez_%C5%82%C4%85czenie_naturalne

def divide_into_series(first: Node):
    # Umieszczanie posortowanych serii w tabeli
    T = []
    while first != None:
        T.append(first)
        prev = first
        first = first.nxt
        while first != None and prev.val <= first.val:
            prev = first
            first = first.nxt
        prev.nxt = None
    return T


def recursive_merge(T, l, r):
    if (r-l) <= 1:
        return T[l]
    mid = (l + r)//2
    recursive_merge(T, l, mid)
    recursive_merge(T, mid, r)
    T[l] = (merge_sorted_lists(T[l], T[mid]))
    return T[l]


def natural_mergesort(first):
    T = divide_into_series(first)
    return recursive_merge(T, 0, len(T))


# Wywołanie:
# natural_mergesort(first)

class Node():
    def __init__(self, val):
        self.val = val
        self.next = None

def bubbleSort(head):

    isSorted = False
    while not isSorted:
        first = head
        isSorted = True

        while first.next != None:
            if first.val > first.next.val:
                value = first.val
                first.val = first.next.val
                first.next.val = value

                isSorted = False

            first = first.next

    return head
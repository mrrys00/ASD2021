class Node():
    def __init__(self, val, nxt):
        self.val = val
        self.nxt = nxt

def reverseList(myListHead):
    if myListHead == None or myListHead.nxt == None:
        return myListHead

    prevNode = None
    currentNode = myListHead
    nextNode = myListHead.nxt
    while nextNode != None:
        currentNode.nxt = prevNode
        prevNode = currentNode
        currentNode = nextNode
        nextNode = nextNode.nxt

    currentNode.nxt = prevNode

    return currentNode
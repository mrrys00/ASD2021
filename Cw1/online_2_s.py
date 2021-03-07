from time import sleep

class Node():
    def __init__(self, val, nxt):
        self.val = val
        self.nxt = nxt

def insertValueToSortedList(myListHead, value):
    if myListHead == None or value < myListHead.val:
        myListHead = Node(val=value, nxt=myListHead)
        return myListHead

    newNode = Node(val=value, nxt=None)
    currentNode = myListHead
    while currentNode.nxt != None:
        if currentNode.val <= newNode.val and newNode.val < currentNode.nxt.val:
            newNode.nxt = currentNode.nxt
            currentNode.nxt = newNode

        currentNode = currentNode.nxt
    
    currentNode.nxt = newNode
    return myListHead

def removeMax(myListHead):
    if myListHead == None:
        return None, None
    if myListHead.nxt == None:
        maxi = myListHead.val
        myListHead = None
        return myListHead, maxi

    beforeMaxNode = None
    beforeNode = myListHead
    currentNode = myListHead.nxt
    maxi = myListHead.val

    while currentNode != None:
        if maxi < currentNode.val:
            maxi = currentNode.val
            beforeMaxNode = beforeNode

        currentNode = currentNode.nxt
        beforeNode = beforeNode.nxt

    if beforeMaxNode == None:
        newHead = myListHead.nxt
        del myListHead
        return newHead, maxi
    
    maxNode = beforeMaxNode.nxt
    beforeMaxNode.nxt = beforeMaxNode.nxt.nxt
    del maxNode
    return myListHead, maxi

#########

def extractMaxNode(myListHead):
    if myListHead == None:
        return None, None
    if myListHead.nxt == None:
        return None, myListHead

    beforeMaxNode = None
    beforeNode = myListHead
    currentNode = myListHead.nxt
    maxi = myListHead.val

    while currentNode != None:
        if maxi < currentNode.val:
            maxi = currentNode.val
            beforeMaxNode = beforeNode

        currentNode = currentNode.nxt
        beforeNode = beforeNode.nxt

    if beforeMaxNode == None:
        newHead = myListHead.nxt
        return newHead, myListHead
    
    maxNode = beforeMaxNode.nxt
    beforeMaxNode.nxt = beforeMaxNode.nxt.nxt
    return myListHead, maxNode

def insertNodeToSortedList(myListHead, node):
    if myListHead == None or node.val < myListHead.val:
        node.nxt = myListHead
        return node

    currentNode = myListHead
    while currentNode.nxt != None:
        if currentNode.val <= node.val and node.val < currentNode.nxt.val:
            node.nxt = currentNode.nxt
            currentNode.nxt = node

        currentNode = currentNode.nxt
    
    node.nxt = currentNode.nxt
    currentNode.nxt = node
    return myListHead

def insertionSortUsingRemoveMaxAndinsertValueToSortedList(myListHead):
    newListHead = None
    while myListHead != None:
        myListHead, maxNode = extractMaxNode(myListHead=myListHead)
        print("max", maxNode.val)
        newListHead = insertNodeToSortedList(myListHead=newListHead, node=maxNode)

    return newListHead
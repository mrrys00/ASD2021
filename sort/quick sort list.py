from random import randint, seed

class Node:
    def __init__(self):
        self.next = None
        self.value = None

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
def whatsTail(head):
    tail = head
    while tail.next: tail = tail.next
    return tail

def qsort(head): return  qsortMain(head)[0]

def qsortMain(head, tail = -1):
    if not head: return head, head
    if tail == -1: tail = whatsTail(head)
    if head == tail: return head, tail
    pivot, head, tail, prev = listPart (head, tail) # prev to node przed pivotem

    #left from pivots
    if not head == pivot:
        #print("\nim in left, head ",head.value,"\tprev ",prev.value)
        #printlist (head)
        prev.next = None
        head, prev = qsortMain(head, prev)
        #print("\nim in left output, head ",head.value,"\tprev ",prev.value)
        #printlist (head)
        prev.next = pivot

    # pivots
    newHead = pivot
    if pivot.next:
        #print ("im in pivots")
        while newHead.next and newHead.next.value == pivot.value: newHead = newHead.next
    
    # right from pivots
    if not newHead == tail: newHead.next, tail = qsortMain(newHead.next, tail)

    #print("\n")
    #printlist(head)
    #print("output\thead ", head)
    return head, tail

def listPart(head, tail):
    pivot, current, prev = tail, head, Node()
    currentIsHead = True
    #print("\n")
    #printlist(head)
    #print("entry \tpivot: ",pivot.value,"\thead: ",head.value,"\tprev: ",prev.value,"\ttail: ",tail.value)
    while current != pivot:
        if currentIsHead:
            if current.value < pivot.value:
                prev = current
                current = current.next
                currentIsHead = False
            elif current.value == pivot.value:
                prev.next = current.next
                head = current.next
                current.next = pivot.next
                pivot.next = current
                if tail == pivot: tail = current
                current = prev.next
            else:
                prev.next = current.next
                head = current.next
                current.next = None
                tail.next = current
                tail = current
                current = prev.next
        else:
            if current.value < pivot.value:
                prev = current
                current = current.next
            elif current.value == pivot.value:
                prev.next = current.next
                current.next = pivot.next
                pivot.next = current
                if tail == pivot: tail = current
                current = prev.next
            else:
                prev.next = current.next
                current.next = None
                tail.next = current
                tail = current
                current = prev.next
    #printlist(head)
    #print("return\tpivot: ",pivot.value,"\thead: ",head.value,"\tprev: ",prev.value,"\ttail: ",tail.value, "\n")
    return pivot, head, tail, prev

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
def tab2list(A):
    H = Node()
    C = H
    for i in range(len(A)):
        X = Node()
        X.value = A[i]
        C.next = X
        C = X
    return H.next

def printlist(L):
    while L != None:
        print( L.value, "->", end=" ")
        L = L.next
    print("|")  

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
seed(42)
n = 10
T = [ randint(1,10) for i in range(10) ]
L = tab2list(T)

print("")
printlist(L) 
L = qsort(L)
print("")
printlist(L)

if L == None:
    print("List jest pusta, a nie powinna!")
    exit(0)

P = L
while P.next != None:
    if P.value > P.next.value:
        print("Błąd sortowania")
        exit(0)
    P = P.next
        
print("OK")
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
'''
def listPart(head, tail): # head / low -->  -->  -->  -->  --> tail / high
    pivot, current, prev, newTail = tail, head, Node(), tail
    
    firstTime = True
    
    bigHead, bigTail = None, None

    printlist(head)
    
    while not current == pivot:
        if firstTime:
            if current.value < pivot.value:
                prev = current
                current = current.next
            
            elif current.value == pivot.value:
                prev.next = current.next
                newTail = current
                newTail.next = None
                pivot.next = newTail
                current = prev.next
                head = current

            if current.value > pivot.value:
                prev.next = current.next
                current.next = None
                bigHead, bigTail = bigListAdd(bigHead, bigTail, current)
                current = prev.next
                head = current
        
        else:
            if current.value < pivot.value:
                prev = current
                current = current.next
            
            elif current.value == pivot.value:
                prev.next = current.next
                newTail = current
                newTail.next = None
                pivot.next = newTail
                current = prev.next
            
            else:
                prev.next = current.next
                current.next = None
                bigHead, bigTail = bigListAdd(bigHead, bigTail, current)
                current = prev.next
        
        firstTime = False
    
    newTail.next = bigHead

    printlist(head)
    print("pivot: ",pivot.value,"\thead: ",head.value,"\tprev: ",prev.value,"\ttail: ",newTail.value)
    return pivot, head, prev, bigTail
    
def bigListAdd (head, tail, newElement):
    if not head: return newElement, newElement
    else: tail.next = newElement
    return head, newElement
    '''
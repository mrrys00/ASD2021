from random import randint, seed


class Node:
  def __init__(self):
    self.next = None
    self.value = None
    

# PROGRAM START
def qs_partition_lists(head, tail):
  prev = Node()
  pivot, last_pivot, prev.next, temp = tail, tail, head, head
  head = prev
  while temp != pivot:
    if temp.value > pivot.value:
      prev.next = temp.next
      temp.next = None
      tail.next = temp
      tail = tail.next
      temp = prev.next
    elif temp.value == pivot.value:
      prev.next = temp.next
      temp.next = pivot.next
      pivot.next = temp
      if tail == pivot:
        tail = tail.next
      temp = prev.next
    else:
      prev = prev.next
      temp = temp.next
  while last_pivot.next != None and last_pivot.value == last_pivot.next.value:
    last_pivot = last_pivot.next
  return head.next, prev, pivot, last_pivot, tail


def quick_sort_lists(head, tail):
  if head.next == None:
    return head, head
  head, prev, pivot, last_pivot, tail = qs_partition_lists(head, tail)
  if prev.value != None:
    prev.next = None
    head, prev = quick_sort_lists(head, prev)
    prev.next = pivot
  if last_pivot.next != None:
    last_pivot.next, tail = quick_sort_lists(last_pivot.next, tail)
  return head, tail
# PROGRAM END


def qsort( L ):
  tail = L
  while tail.next != None:
    tail = tail.next
  L = quick_sort_lists(L, tail)[0]
  return L





def tab2list( A ):
  H = Node()
  C = H
  for i in range(len(A)):
    X = Node()
    X.value = A[i]
    C.next = X
    C = X
  return H.next
  
  
def printlist( L ):
  while L != None:
    print( L.value, "->", end=" ")
    L = L.next
  print("|")

  
  
  

seed(42)

n = 10
T = [ randint(1,10) for i in range(10) ]
L = tab2list( T )

print("przed sortowaniem: L =", end=" ")
printlist(L) 
L = qsort(L)
print("po sortowaniu    : L =", end=" ")
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


from random import randint, seed


def merge(T, l, r):
  if (r-l) <= 1: # Warunek przerwania rekurencji
    return T # Nie trzeba zwracać T
  mid = (l + r)//2 # Tablica lewa <= prawej
  merge(T, l, mid) # Rekurencja dla lewej strony 
  merge(T, mid, r) # Rekurencja dla prawej strony 
  tab = [T[i] for i in range(l,mid)] # Kopiowanie lewej strony do tablicy pomocniczej
  i = 0 # Przechodzi po lewej stronie (tablicy pomocniczej)
  j = mid # Przechodzi po prawej stronie (nieskopiowanej)
  mid = j - l # wyznacza długość tablicy pomocniczej
  while i < mid and j < r: # Scalanie
    if tab[i] <= T[j]:
      T[l] = tab[i]
      i += 1
    else:
      T[l] = T[j]
      j +=1
    l += 1
  while i < mid: #Jeśli pozostały elementy w tablicy pomocniczej
    T[l] = tab[i] # Kopiujemy je do oryginalnej tablicy
    i += 1; l += 1 
  return T # Nie trzeba zwracać T
  
  
def mergesort(T):
  return merge(T, 0, len(T))
  
  
  

seed(42)

n = 10
T = [ randint(1,10) for i in range(10) ]

print("przed sortowaniem: T =", T) 
T = mergesort(T)
print("po sortowaniu    : T =", T)

for i in range(len(T)-1):
  if T[i] > T[i+1]:
    print("Błąd sortowania!")
    exit()
    
print("OK")

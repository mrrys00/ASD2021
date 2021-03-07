def findMinMax(lista):
    mini = float("inf")
    maxi = -float("inf")

    listLength = len(lista)

    if listLength % 2 == 0:                     # even length
        for i in range(0, listLength, 2):
            if lista[i] < lista[i+1]:
                mini = min(mini, lista[i])
                maxi = max(maxi, lista[i+1])
            else:
                mini = min(mini, lista[i+1])
                maxi = max(maxi, lista[i])  
    else:                                       # odd length
        for i in range(0, len(lista)-1, 2):
            if lista[i] < lista[i+1]:
                mini = min(mini, lista[i])
                maxi = max(maxi, lista[i+1])
            else:
                mini = min(mini, lista[i+1])
                maxi = max(maxi, lista[i])

        maxi = max(maxi, lista[listLength-1])
        mini = min(mini, lista[listLength-1])

    return mini, maxi
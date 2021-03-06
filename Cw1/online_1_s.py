def selectSort(t):
    length = len(t)

    for i in range(length-1):
        minElem = i
        for j in range(i+1, length):
            if t[j] < t[minElem]:
                minElem = j

        key = t[minElem]
        t[minElem] = t[i]
        t[i] = key

    return t

def bubbleSort(t):
    length = len(t)

    for index in range(length-1):
        index2 = index
        while t[index2] > t[index2+1] and index2 >= 0:
            t[index2], t[index2+1] = t[index2+1], t[index2]
            index2 -= 1

    return t

# t = bubbleSort([5,3,2,7,1])
# print(t)
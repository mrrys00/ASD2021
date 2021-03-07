def largestIncSeq(array):
    score = [1] * len(array)
    parent = [-1] * len(array)
    for i in range(len(array)):
        for j in range(i):
            if array[j] < array[i] and score[j] + 1 > score[i]:
                score[i] = score[j] + 1
                parent[i] = j
    
    first = score.index(max(score))
    output = []
    while not first == -1:
        output.insert(0, array[first])
        first = parent [first]
    return output

array = [1, 3, 5, 7, 0, 0, 9, 4]
print (largestIncSeq (array))
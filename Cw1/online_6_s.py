def binarySearch(array, x):
    start = 0
    end = len(array) - 1

    while start < end:
        middle = (end+start)//2
        if array[middle] == x:
            while array[middle] == array[middle-1] and middle > 0:
                middle -= 1
            return middle
        elif array[middle] < x:
            start = middle
        else:
            end = middle
    
    return None

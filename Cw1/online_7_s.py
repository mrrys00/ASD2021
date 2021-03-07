def checkIfExistTwoIndexesSumToSpecifiedNumber(array, expectedSum):
    start = 0
    end = len(array) - 1

    while start < end:
        if expectedSum == array[start] + array[end]:
            return start, end, True
        elif expectedSum > array[start] + array[end]:
            start += 1
        else:
            end -= 1
    
    return None, None, False
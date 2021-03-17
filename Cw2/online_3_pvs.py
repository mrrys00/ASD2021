def find_sum_equal_to_given_val(T, val):
    # Oryginalne zadanie
    i, j = 0, len(T)-1
    while i < j:
        if val > T[i] + T[j]:
            i += 1
        elif val < T[i] + T[j]:
            j -= 1
        else:
            return i, j
    return -1, -1


def find_sum(A):
    # modyfikacja A[i1]+A[j1]=A[i2]+A[j2]
    if len(A) < 4:
        return False
    for start in range(0, len(A)):
        for end in range(start+1, len(A)):
            x = A[start] + A[end]
            i = start + 1
            j = end - 1
            while i < j:
                if x == A[i] + A[j]:
                    return start, end, i, j  # True
                if x > A[i] + A[j]:
                    i += 1
                else:
                    j -= 1
    return False


t = [1, 5, 6, 8, 9, 13, 15, 16, 18]
print(find_sum(t))

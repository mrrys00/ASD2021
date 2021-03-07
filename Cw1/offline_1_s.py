from random import randint, seed



def merge(leftArray, rightArray):
	lPointer, rPointer = 0, 0
	leftLen, rightLen = len(leftArray), len(rightArray)
	resultArray = [ None for _ in range(leftLen + rightLen) ]

	print("to merge: ", leftArray, rightArray)

	while lPointer < leftLen and rPointer < rightLen:
		if leftArray[lPointer] < rightArray[rPointer]:
			print("l < r")
			resultArray[lPointer+rPointer] = leftArray[lPointer]
			lPointer += 1
		elif leftArray[lPointer] == rightArray[rPointer]:
			print("l = r")
			resultArray[lPointer + rPointer] = leftArray[lPointer]
			resultArray[lPointer + rPointer + 1] = rightArray[rPointer]
			lPointer, rPointer = lPointer+1, rPointer+1
		else:
			print("l > r")
			resultArray[lPointer + rPointer] = rightArray[rPointer]
			rPointer += 1

	print("rest after sort: ", leftArray[:lPointer], rightArray[:rPointer])
	print("pointers: ", lPointer, rPointer)

	while lPointer < leftLen: 
		resultArray[lPointer + rPointer] = leftArray[lPointer]
		lPointer += 1
	while rPointer < rightLen:
		resultArray[lPointer + rPointer] = rightArray[rPointer]
		rPointer += 1

	return resultArray

def mergesort(T):
	length = len(T)
	if length > 1:
		separator = length // 2
		print("separator: ", separator, "arrays after separate: ", T[:separator], T[separator:])
		T = merge(mergesort([ T[i] for i in range(0, separator) ]), mergesort( [ T[i] for i in range(separator, length) ] ) )
		print("part merge: ", T)
	return T

seed(42)

n = 10
T = [ randint(1,10) for i in range(150	) ]

print("przed sortowaniem: T =", T) 
T = mergesort(T)
print("po sortowaniu    : T =", T)

for i in range(len(T)-1):
	if T[i] > T[i+1]:
		print("Błąd sortowania!")
		exit()
    
print("OK")
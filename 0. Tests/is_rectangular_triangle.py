def isTriplet(array, n):
	for i in range(n):
		array[i] = array[i] * array[i]
	array.sort()


	for i in range(n-1, 1, -1):
		j = 0
		k = i - 1
		while (j < k):
			if (array[j] + array[k] == array[i]):
				return True
			else:
				if (array[j] + array[k] < array[i]):
					j = j + 1
				else:
					k = k - 1
	return False

array = [3,4,5]
array_size = len(array)
if(isTriplet(array, array_size)):
	print("True")
else:
	print("False")
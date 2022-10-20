array = [3,4,5]
array_size = len(array)

def rectangular_triangle(array, x): #Takes two arguments, an array (list) and second argument
	for i in range(x): # for every element in range
		array[i] = array[i] * array[i] #  Square each element of the array
	array.sort() # Sort the squared aray in ascending order


	for i in range(x-1, 1, -1):
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

print(rectangular_triangle(array, array_size))


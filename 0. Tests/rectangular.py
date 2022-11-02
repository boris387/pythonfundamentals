array = [2,9,11,5,7,24,13,25,69]
array_size = len(array)

def multiplication(n):
    return n * n

array = sorted(list(map(multiplication, array)))

def rectangular_triangle(array, x): #Takes two arguments, an array (list) and second argument
	 #Map() iterates over the array and applies function to every element, then since Map() does not support sorted, it is converted to list and then sorted
	for i in range(x-1, 1, -1):
		j = 0
		k = i - 1
		while (j < k):
			if (array[j] + array[k] == array[i]):
				return True, array[j], array[k], array[i]
			else:
				if (array[j] + array[k] < array[i]):
					j = j + 1
				else:
					k = k - 1
	return False

print(rectangular_triangle(array, array_size))
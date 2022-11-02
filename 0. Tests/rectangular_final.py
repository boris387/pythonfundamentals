# import math, random

# def get_num_triplets(array):
#     result2 = math.factorial(len(array))/(math.factorial(3)*math.factorial((len(array)-3)))
#     return result2

# def is_rectangular_triangle(triplet):
#     if len(triplet) != 3:
#         print("Three sides are expected as an input")
#         return
#     triplet = triplet.copy()
#     max_index = triplet.index(max(triplet))
#     hypothenus = triplet.pop(max_index)
#     result = triplet[0]**2 + triplet[1]**2 == hypothenus**2
#     return result

# def new_function(short_list,max_iter=1000):
#     viewed_triplets = []
#     i = 0
#     iter = 0 #horrible name
#     while i < get_num_triplets(short_list):
#         random_list = sorted(random.sample(short_list,3))
#         if random_list not in viewed_triplets:
#             if is_rectangular_triangle(random_list):
#                 print(random_list, "Is a rectangular triangle") # Create a set to avoid duplications, {}
#             viewed_triplets.append(random_list)
#             i +=1
#         iter +=1
#         if iter >= max_iter:
#             break

# short_list = [2,9,11,5,7,24,13,25,69,12,3,4,5,15,25,75,18,34,69,54]


# for x in range(10):
#     new_function(short_list)

# print(get_num_triplets(short_list))

# all_triplets = [[3,4,5], [5,12,13], [5,12,13], [21, 18, 38]]
# for x in all_triplets: # if x is an rectangular triangle, print "x = rectangular triangle"
#     if is_rectangular_triangle(x):
#         print(x, "Is a rectangular triangle")

# short_list = [1,2,3,4]
# combinations = []
# for element in short_list:
#     triplet = [element]


# print(is_rectangular_triangle(all_triplets))

array = [5,12,13,3,7]

def func(x):
    return x

lambda x: x


def multiplication(n):
    return n * n
    

n = lambda x,y: x*y

print(n(5,5))

x = lambda a : a + 10
print(x(5))

array = sorted(list(map(multiplication, array)))
array = sorted(list(map(lambda x: x*x, array)))


def rectangular_triangle(array): #Takes two arguments, an array (list) and second argument
	 #Map() iterates over the array and applies function to every element, then since Map() does not support sorted, it is converted to list and then sorted
	for i in range(len(array)-1, 1, -1):
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
    
print(rectangular_triangle(array))


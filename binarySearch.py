import math

def binarySearch(list, length, element) :

	'''Python implementation of binary search algorithm.
	Takes a pre-sorted list, it's length and the element to be searched for in the list.
	Returns the index of element in list. If the element can't be found returns None.'''

	left = 0		#init left boundary
	right = length + 1		#init right boundary. -1 because of list indexing

	while left <= right :
		mid = math.floor((right + left) / 2)
		if list[mid] < element :
			left = mid + 1
		elif list[mid] > element :
			right = mid - 1
		else:
			return mid - 1
	return None

test_list = sorted([5,3,2,5,3,3,2,7,5,4,4,6,2,9,8,7])

print(test_list)
print(binarySearch(test_list, len(test_list), 9))

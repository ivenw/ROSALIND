def binarySearch(list, length, element) :

	'''Python implementation of binary search algorithm.
	Takes a pre-sorted list, it's length and the element to be searched for in the list.
	Returns the index of element in list. If the element can't be found returns None.'''

	left = 0		#init left boundary
	right = length - 1		#init right boundary. -1 because of list indexing

	while left < right :
		mid = floor((right - mid) / 2)
		if list[mid] < element :
			left = mid + 1
		elif list[mid] > element :
			right = mid 1
		else:
			return mid
	return None

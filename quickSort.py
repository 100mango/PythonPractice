#coding=utf-8
import random

def quickSort(array):
	less = []
	equal = []
	greatter = []

	if len(array) <= 1:
		return array
	else:
		pivot = array[0]    #random.choice(array) 更好
		for element in array:
			if element < pivot:
				less.append(element)
			if element == pivot:
				equal.append(element)
			if element > pivot:
				greatter.append(element)
		return quickSort(less) + equal + quickSort(greatter)


sortArray =  quickSort([2,3,1,43,54,2,45,67,11,2,4,6,7,8])

print sortArray
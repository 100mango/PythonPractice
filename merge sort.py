#coding = utf-8

def merge(leftArray,rightArray):

	mergedArray = [] 

	while leftArray and rightArray:
		mergedArray.append(leftArray.pop(0) if leftArray[0] <= rightArray[0] else rightArray.pop(0))
	while leftArray:
		mergedArray.append(leftArray.pop(0))
	while rightArray:
		mergedArray.append(rightArray.pop(0))

	return mergedArray

def mergeSort(array):

	if len(array) <= 1:
		return array

	middle = int(len(array)/2)
	leftArray = mergeSort(array[:middle])   #归并排序是一个分治算法  递归自顶向下求解
	rightArray = mergeSort(array[middle:])

	return merge(leftArray, rightArray)
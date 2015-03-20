#coding=utf-8

def merge(leftArray,rightArray):

	mergedArray = [] 

	while leftArray and rightArray:
		mergedArray.append(leftArray.pop(0) if leftArray[0] <= rightArray[0] else rightArray.pop(0))
	while leftArray:
		mergedArray.append(leftArray.pop(0))
	while rightArray:
		mergedArray.append(rightArray.pop(0))

	return mergedArray

def mergeRecursively(leftArray,rightArray):
    if len(leftArray) == 0 :
        return rightArray
    elif len(rightArray) == 0:
        return leftArray

    mergedArray = []
    if leftArray[0] < rightArray[0]:
        mergedArray.append(leftArray.pop(0))
        mergedArray.extend(mergeRecursively(leftArray,rightArray))
    else:
        mergedArray.append(rightArray.pop(0))
        mergedArray.extend(mergeRecursively(leftArray,rightArray))
    return mergedArray
 
def mergeSort(array):

	if len(array) <= 1:
		return array

	middle = len(array)//2
	leftArray = mergeSort(array[:middle])  #归并排序是一个分治算法  递归自顶向下求解
	rightArray = mergeSort(array[middle:]);
    return mergeRecursively(leftArray, rightArray)
	#return merge(leftArray, rightArray)
print mergeSort([10,9,8,7,6,5,4,3,2,1])


#leetcode 
#Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param two ListNodes
    # @return a ListNode
    def mergeTwoLists(self, l1, l2):
        dummy = ListNode(-1)    #构造链表时，没有第一个数据 先构造一个假数据作为头
        currentPointer = dummy
        while l1 and l2:
            if l1.val <= l2.val:
                currentPointer.next = l1
                l1 = l1.next
            else:
                currentPointer.next = l2
                l2 = l2.next
            currentPointer = currentPointer.next
        if l1 is not None:
            currentPointer.next = l1
        if l2 is not None:
            currentPointer.next = l2
        return dummy.next
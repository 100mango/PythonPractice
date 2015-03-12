#coding=utf-8

#如果成功则返回找到的数字，否则返回false  递归实现
def binarySearch(list,value):

	if list is None:
		return False

	low = 0 
	high = len(list) - 1;mid = (high + low)//2

	if low <= high:
		if value == list[mid]:
			return list[mid]
		elif value < list[mid]:
			return binarySearch(list[:mid], value)
		else:
			return binarySearch(list[mid + 1:], value)
	#若找不到 则retuen false		
	return False

print binarySearch([1,2,3,4,5,6,7,8,9,10], 11)

#返回下标的形式 非递归实现  若失败 返回false
def binarySearchSecond(array,value):

	low = 0
	high = len(list) - 1

	while low <= high:
		mid = (low + high)//2
		if value == array[mid]:
			return mid
		elif value < array[mid]:
			high = mid - 1
		else:
			low = mid + 1

	return False


'''
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Here are few examples.
[1,3,5,6], 5 → 2
[1,3,5,6], 2 → 1
[1,3,5,6], 7 → 4
[1,3,5,6], 0 → 0
'''

class Solution:
    # @param A, a list of integers
    # @param target, an integer to be inserted
    # @return integer
    def searchInsert(self, A, target):
        low = 0
    	high = len(A) - 1
    
    	while low <= high:
    		mid = (low + high) // 2
    		if target == A[mid]:
    			return mid
    		elif target < A[mid]:
    			high = mid - 1
    		else:
    		    low = mid + 1
    		return low   #退出递归的原因是 low > high 此时的Low 即为下标 


'''
Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

You may assume no duplicate exists in the array.
'''

class Solution2:
    # @param num, a list of integer
    # @return an integer
    def findMin(self, num):

    	left = 0;
    	right = len(num) - 1

    	while num[left] > num[right]:
    		mid = (left + right)//2
    		if num[mid] >= num[left]:   #需要注意边界条件 大于等于 有可能mid = left 例如array长度为2
    			left = mid + 1
    		else: # num[mid] <num[right]:
    			right = mid

    	return num[left]


'''
Follow up for "Find Minimum in Rotated Sorted Array":
What if duplicates are allowed?

Would this affect the run-time complexity? How and why?
Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

The array may contain duplicates.
'''






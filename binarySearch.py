#coding=utf-8

#如果成功则返回找到的数字，否则返回false
def binarySearch(list,value):

	if list is None:
		return False

	low = 0
	high = len(list) - 1

	while low <= high:
		mid = (low + high) // 2
		if value == list[mid]:
			return list[mid]
		elif value < list[mid]:
			return binarySearch(list[:mid], value)
		else:
			return binarySearch(list[mid + 1:], value)
	#若找不到 则retuen false		
	print False

print binarySearch([1,2,3,4,5,6,7,8,9,10], 11)

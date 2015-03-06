#coding:utf-8

#剑指offer：第三题
#题目：在一个二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。


matrix = [[1, 2, 8, 9],
    [2, 4, 9, 12],
    [4, 7, 10, 13],  
    [6, 8, 11, 15],]


def find(matrix,value):
	if matrix is None:
		return False
	row = 0   #初始化位置为matrix右上角
	columns = len(matrix[0]) - 1

	while row < len(matrix) and columns >= 0:
		if value < matrix[row][columns]:
			columns = columns - 1
		elif value > matrix[row][columns]:
			row = row + 1
		else:
			return True
	return False

print find(matrix, 20)


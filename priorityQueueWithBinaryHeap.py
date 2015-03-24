#coding=utf8

class binaryHeap():
	def __init__(self):
		self.heapList = [0]   #第一个节点不需要使用，用于维护二插堆满二叉树属性
		self.currentSize = 0

	def insert(self,value):
		self.heapList.append(value)    #创建一个新的节点
		self.currentSize = self.currentSize + 1
		index = self.currentSize

		while index > 1: 
			if self.heapList[index//2] > value: #如果父节点大于新元素，则父节点移动至下面，直至新元素找到位置 
				self.heapList[index] = self.heapList[index//2] #这种做法避免了不断交换的低效性
			else:
				break   #找到位置
			index = index//2

		self.heapList[index] = value

	def deleteMin(self):
		if self.currentSize == 0:
			return None

		min = self.heapList[1] 
		lastElement = self.heapList[self.currentSize]
		self.heapList.pop() #删除最后一个元素，准备将它移动至正确位置
		self.currentSize = self.currentSize - 1
		index = 1 

		while index*2 <= self.currentSize: #从第一个位置开始，如果还有子节点，则不断向下将子节点移动上来
			minChindIndex = self.minIndex(index) 
			if lastElement > self.heapList[minChindIndex]:
				self.heapList[index] = self.heapList[minChindIndex]
			else:
				break 
			index = minChindIndex
			
		self.heapList[index] = lastElement
		return min

	def minIndex(self,index): 
		if index*2 + 1 > self.currentSize:
			return index*2
		else:
			if self.heapList[index*2] > self.heapList[index*2+1]:
				return index*2 + 1
			else:
				return index



binaryHeap = binaryHeap()
binaryHeap.insert(10)
binaryHeap.insert(9)
binaryHeap.insert(8)
binaryHeap.insert(7)
binaryHeap.insert(6)
binaryHeap.insert(5)
binaryHeap.insert(4)

print binaryHeap.heapList
print binaryHeap.deleteMin()

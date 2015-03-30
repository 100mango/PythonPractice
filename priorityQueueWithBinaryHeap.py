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
		if index*2 + 1 > self.currentSize: #只有右节点
			return index*2
		else:
			if self.heapList[index*2] > self.heapList[index*2+1]:
				return index*2 + 1
			else:
				return index*2

	def percolateUp(self,index):
		while index//2 > 0: #从index 不断上滤
			if self.heapList[index] < self.heapList[index//2]:
				temp = self.heapList[index//2]
				self.heapList[index//2] = self.heapList[index]
				self.heapList[index] = temp
			index = index//2


	def insertTwo(self,value): #易懂交换版本
		self.heapList.append(value)
		self.currentSize = self.currentSize + 1
		self.percolateUp(self.currentSize)

	def percolatwDown(self,index):
		while index*2 <= self.currentSize:
			minIndex = self.minIndex(index)
			if self.heapList[index] > self.heapList[minIndex]:
				temp = self.heapList[minIndex]
				self.heapList[minIndex] = self.heapList[index]
				self.heapList[index] = temp
			index = minIndex

	def deleteMinTwo(self):
		min = self.heapList[1]
		self.heapList[1] = self.heapList[self.currentSize]
		self.heapList.pop()
		self.currentSize = self.currentSize - 1
		self.percolatwDown(1)
		return min

	def buildHeap(self,array):
		self.currentSize = len(array)
		self.heapList.extend(array)
		i = len(array)//2
		while i > 0:
			print i
			self.percolatwDown(i)
			i = i - 1
		print 'done'

#算法来自数据结构与算法分析 C语言描述 第二版 堆排序部分
#通常堆是通过一维数组来实现的。在起始数组为0的情形中：
#父节点i的左子节点在位置(2*i+1);
#父节点i的右子节点在位置(2*i+2);
	def maxIndex(self,heap,index,heapLength):
		if index*2 + 2 > heapLength-1:
			return index*2+1
		else:
			if heap[index*2+1] < heap[index*2+2]:
				return index*2+2
			else:
				return index*2+1

	def maxHeapPercolateDown(self,heap,index,heapLength):
		while index*2+1 <= heapLength-1:
			maxIndex = self.maxIndex(heap, index, heapLength)
			if heap[index] < heap[maxIndex]:
				temp = heap[index]
				heap[index] = heap[maxIndex]
				heap[maxIndex] = temp
			index = maxIndex

	def heapSort(self,array):
		lenth = len(array)

		i = lenth//2
		while i >= 0: #建立最大堆
			self.maxHeapPercolateDown(array, i, lenth)
			i = i - 1

		i = lenth - 1
		while i > 0: 
			temp = array[i]
			array[i] = array[0]
			array[0] = temp
			self.maxHeapPercolateDown(array, 0, i) #第一次交换后 heap长度就已经是lenth-1了
			i = i - 1

		return array

binaryHeap = binaryHeap()
binaryHeap.buildHeap([10,9,8,7,6,5,4])


print binaryHeap.heapList
print binaryHeap.deleteMinTwo()
print binaryHeap.deleteMinTwo()
print binaryHeap.heapList

print binaryHeap.heapSort([10,9,8,7,110,100,90])

#leetcode Merge k Sorted Lists  堆版本
class Solution:
    # @param a list of ListNode
    # @return a ListNode
    def mergeKLists(self, lists):
        heap = []
        for listNode in lists:
            if listNode is not None:
                heap.append((listNode.val,listNode))
        heapq.heapify(heap)
        dummy = ListNode(0) 
        current = dummy
        while heap:
            popItem = heapq.heappop(heap)
            current.next = popItem[1]
            current = current.next
            if current.next is not None:
                heapq.heappush(heap,(current.next.val,current.next))
        return dummy.next
        


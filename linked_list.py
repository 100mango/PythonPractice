#coding=utf-8

class Node:

	def __init__(self, data):
		self.data = data
		self.nextNode = None

	def __str__(self):
		return str(self.data)

class linkedList:
	def __init__(self, headNode = None):
		self.headNode = headNode

	def printList(self):
		node = self.headNode
		while node is not None:
			print node.data
			node = node.nextNode
		
	def insert(self,node):  #O(1)
		if self.headNode is None:
			self.headNode = node
		else:
			node.nextNode = self.headNode
			self.headNode = node

	def  find(self,data):
		node = self.headNode

		while node is not None:
			if data == node.data:
				return node
			else:
				node = node.nextNode

		return False

	def delete(self,data):

		if self.headNode is None:
			raise ValueError('list is empty')

		currentNode = self.headNode
		previousNode = None

		while currentNode is not  None:
			if currentNode.data == data:
				if previousNode is not None:
					previousNode.nextNode = currentNode.nextNode
				else: #如果是头结点 则直接将头结点指向下一个
					self.headNode = currentNode.nextNode
			else:
				previousNode = currentNode
				currentNode = currentNode.nextNode

linkedList = linkedList()
linkedList.insert(Node(1))
linkedList.insert(Node(10))
linkedList.insert(Node(12))
linkedList.insert(Node(5))
linkedList.insert(Node(8))

#linkedList.printList()
linkedList.delete(12)
linkedList.printList()






#coding:utf-8

class Node:

	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

	def insert(self,data):
		if self.data == None:
			self.data = data
		else
			if data < self.data:
				if self.left is None:
					self.left = Node(data)
				else
					self.left.insert(data)
			elif data > self.data:
				if self.right is None:
					self.right = Node(data)
				else
					self.right = Node(data)


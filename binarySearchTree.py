#coding:utf-8

class Node:

	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

	def __str__(self):
		return str(self.data)

	def insert(self,data):
		if self.data == None:
			self.data = data
		else:
			if data < self.data:
				if self.left is None:
					self.left = Node(data)
				else:
					self.left.insert(data)
			elif data > self.data:
				if self.right is None:
					self.right = Node(data)
				else:
					self.right = Node(data)

	def find(self,data,node):
		if node is None:
			return None
		elif data < node.data:
			return node.find(data,node.left)
		elif data > node.data:
			return node.find(data,node.right)
		else:
		    return node


root = Node(8)
root.insert(3)
root.insert(10)
root.insert(1)
root.insert(6)
root.insert(4)
root.insert(7)
root.insert(14)
root.insert(13)

findedNode =  root.find(7, root)
#print findedNode.data
print root.find(8, root)

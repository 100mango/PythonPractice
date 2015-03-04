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
					self.right.insert(data)

	def find(self,data,node):
		if node is None:
			return None
		elif data < node.data:
			return self.find(data,node.left)
		elif data > node.data:
			return self.find(data,node.right)
		else:
			return node

	def preorder(self,node):
		if node is not None:
			print node.data
			self.preorder(node.left)
			self.preorder(node.right)

	def inorder(self,node):
		if node is not None:
			self.inorder(node.left)
			print node.data
			self.inorder(node.right)

	def postorder(self,node):
		if node is not None:
			self.postorder(node.left)
			self.postorder(node.right)
			print node.data


root = Node(8)
root.insert(3)
root.insert(10)
root.insert(1)
root.insert(6)
root.insert(4)
root.insert(7)
root.insert(14)
root.insert(13)

#print root.find(7, root)

#root.preorder(root)
#root.inorder(root)
root.postorder(root)


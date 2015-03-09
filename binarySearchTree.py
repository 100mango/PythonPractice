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

	#遍历二叉树
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

def compareTwoTree(treeOne,treeTwo):
	if treeOne is None and treeTwo is None:
		return True
	elif treeOne is None or treeTwo is None:
		return False
	elif treeOne.data != treeTwo.data:
		return False
	else:# data已经相等
		leftResult = compareTwoTree(treeOne.left, treeTwo.left)
		rightResult = compareTwoTree(treeOne.right, treeTwo.right)
		return (leftResult and rightResult)


# @param preorder, a list of integers
# @param inorder, a list of integers
# @return a tree node
#leet code Construct Binary Tree from Preorder and Inorder Traversal

def bulidTreeWithPreorderAndInorder(preorder,inorder):
	if preorder is None:
		return None
	else:
		rootNode = Node(preorder[0])
		rootIndex = inorder.index(preorder[0])
		rootNode.left = bulidTreeWithPreorderAndInorder(preorder[1:rootIndex +1 ], inorder[:rootIndex]) #前序遍历序列的根为第一个，随后跟着的是左子树。所以只需知道左子树数量即可获取前序遍历序列的左子树
		rootNode.right = bulidTreeWithPreorderAndInorder(preorder[rootIndex +1: ], inorder[rootIndex + 1:])
		return rootNode

# list slice for inorder and postorder will cost a lot of memory
# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

''' 在Leetcode上的写法
class Solution:
    # @param preorder, a list of integers
    # @param inorder, a list of integers
    # @return a tree node
    def buildTree(self, preorder, inorder):
        if inorder is None or len(inorder) == 0:
            return None
        else:
            rootNodeValue = preorder.pop(0)
		    rootNode = TreeNode(rootNodeValue)
		    rootIndex = inorder.index(rootNodeValue)
		    rootNode.left = self.buildTree(preorder, inorder[:rootIndex]) 
		    rootNode.right = self.buildTree(preorder, inorder[rootIndex + 1:])
		    return rootNode
'''

root = Node(8)
root.insert(3)
root.insert(10)
root.insert(1)
root.insert(6)
root.insert(4)
root.insert(7)
root.insert(14)
root.insert(13)

rootTwo = Node(8)
rootTwo.insert(3)
rootTwo.insert(10)
rootTwo.insert(1)
rootTwo.insert(6)
rootTwo.insert(4)
rootTwo.insert(7)
rootTwo.insert(14)
rootTwo.insert(12)
#print root.find(7, root)

#root.preorder(root)
#root.inorder(root)
#root.postorder(root)

print compareTwoTree(root, rootTwo)


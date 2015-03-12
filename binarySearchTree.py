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

	def preorderInteratively(self,node):
		if node is None:
			return None
		else:
			stack = []
			stack.append(node)
			while len(stack) > 0:
				node = stack.pop()
				print node.data
				if node.right is not None:
					stack.append(node.right) #这里需要主要 利用栈先进后出的特性来模拟递归。 后访问的右节点先进
				if node.left is not None:
					stack.append(node.left)

	def inorder(self,node):
		if node is not None:
			self.inorder(node.left)
			print node.data
			self.inorder(node.right)

'''
前序和中序都是非常简单的，当遇到一个非空的根结点时，打印其数据（如果是前序遍历），并将其压栈，
然后递归地（这里用循环来模拟递归）处理其左子结点；
当没有左子结点时，从栈中弹出之前遇到的某个根结点（它没有左子结点，或者左子结点已经处理完毕，需要再处理右子结点），
打印数据（如果是中序遍历），然后继续处理右子结点。
'''
	def inorderInteratively(self,node):
		if node is None:
			return None
		else:
			stack = []
			while node or stack:
				if node: #不断深入
					stack.append(node)
					node = node.left
				else: #处理节点
					node = stack.pop()
					print node.data
					node = node.right


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
#root.preorderInteratively(root)
root.inorder(root)
root.inorderInteratively(root)
#root.postorder(root)

print compareTwoTree(root, rootTwo)

root.preorderInteratively(root)


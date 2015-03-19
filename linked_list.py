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

		while currentNode is not None:

			if currentNode.data == data:
				if previousNode is not None:
					previousNode.nextNode = currentNode.nextNode
				else: #如果是头结点 则直接将头结点指向下一个
					self.headNode = currentNode.nextNode
			previousNode = currentNode
			currentNode = currentNode.nextNode

linkedList = linkedList()
linkedList.insert(Node(1))
linkedList.insert(Node(10))
linkedList.insert(Node(12))
linkedList.insert(Node(5))
linkedList.insert(Node(8))

#linkedList.printList()
#linkedList.delete(12)
#linkedList.printList()


#剑指offer 面试题5 从尾到头打印链表
def printListFromTail(linked_list):
	stack = []
	if linked_list is not None:
		node = linked_list.headNode
		while node is not None:
			stack.append(node.data)
			node = node.nextNode
		while len(stack) > 0 :
			print stack.pop()

def printListFromTailRecursively(linked_list):
	if linked_list.headNode is None:
		print headNode is None
	if linked_list.nextNode is not None:
		printListFromTailRecursively(linked_list.nextNode)
	print linked_list.data
		

linkedList.printList()
printListFromTail(linkedList)
printListFromTail(linkedList)
	


#leetcode
#Sort a linked list using insertion sort.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#普通插入排序：
def insertion_sort(array):
	for i in range(1,len(array)): #假设第一个已经排好,从第二个开始往前插入
		temp = array[i]
		j = i -1
		while j >= 0 and array[j] > temp:
			array[j + 1] = array[j]
			j = j - 1
		array[j+1] = temp    #需要加1 因为循环最后-1



class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def insertionSortList(self, head):
    	if head is None or head.next is None:
    		return head
    	else:
    		dummy = ListNode(0)
    		dummy.next = head
    		currentNode = head
    		while currentNode.next:
    			if currentNode.next.val > currentNode.val:
    				currentNode = currentNode.next
    			else: #寻找合适位置插入
    				previousNode = dummy
    				while previousNode.next.val < currentNode.next.val:
    					previousNode = previousNode.next
    				temp = currentNode.next
    				currentNode.next = temp.next
    				temp.next = previousNode.next
    				previousNode.next = temp
    		return dummy.next






'''
Given a linked list, remove the nth node from the end of list and return its head.

For example,

   Given linked list: 1->2->3->4->5, and n = 2.

   After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:
Given n will always be valid.
Try to do this in one pass.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @return a ListNode
    def removeNthFromEnd(self, head, n):
        #我们希望指向的是倒数第N+1个节点，这样直接p.next = p.next.next即可完成删除，
        #但是若N刚好是链表长度，那就是头结点，需要引入一个假节点
        #需要指向倒数第N+1个节点，所以前面的指针需要指向顺序第N+1个
        dummy = ListNode(0)
        dummy.next = head
        first =dummy
        second = dummy
        
        for i in range(0,n):
            first = first.next
        while first.next is not None:
            first = first.next
            second = second.next
        second.next = second.next.next
        return dummy.next
          

#Linked List Cycle   leetcode

class Solution:
    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head):
        if head is None:
            return False
        fast = head
        slow = head
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
            if fast is slow:
                return True
        return False
        
            
        


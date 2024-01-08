""" 
2. Add Two Numbers
Medium

You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself. 

Example 1:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
 

Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.

"""

from typing import Optional

# Definition for singly-linked list.
class ListNode: # defined in leet code execution
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class LinkedList: # defined in leet code execution
	def __init__(self):
		self.head = None
		self.tail = None

	def insert(self, val):
		if self.head is None:
			self.head = ListNode(val)
			self.tail = self.head
		else:
			self.tail.next = ListNode(val)
			self.tail = self.tail.next
               
class AddTwoNumbers:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy
        carry = 0

        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            #new digit
            val = v1 + v2 + carry
            #15
            carry = val // 10 # divide
            val = val % 10 # mod formula
            cur.next = ListNode(val)

            #update ptrs
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None 
        # 8 + 7
        return dummy.next

# Utility function to print the list
# Not needed in leet code execution
def printList(n):
	while n:
		print(n.val, end = ' ')
		n = n.next
	print()

# Driver Code
if __name__ == "__main__":
	arr1 = [2,4,3]  # Need to convert the array to ListNode
	LL1 = LinkedList()
	for i in arr1:
		LL1.insert(i)
	print("First list is", end = " ")
	printList(LL1.head)

	arr2 = [5,6,4] # Need to convert the array to ListNode
	LL2 = LinkedList()
	for i in arr2:
		LL2.insert(i)
	print("Second list is", end = " ")
	printList(LL2.head)

	# Function Call
	res = AddTwoNumbers().addTwoNumbers(LL1.head, LL2.head) # ListNode is required to be passed.
	print("Resultant list is", end = " ")
	printList(res)
	print ("")

	arr1 = [7, 5, 9, 4, 6]
	LL1 = LinkedList()
	for i in arr1:
		LL1.insert(i)
	print("First list is", end = " ")
	printList(LL1.head)

	arr2 = [8, 4]
	LL2 = LinkedList()
	for i in arr2:
		LL2.insert(i)
	print("Second list is", end = " ")
	printList(LL2.head)

	# Function Call
	res = AddTwoNumbers().addTwoNumbers(LL1.head, LL2.head)
	print("Resultant list is", end = " ")
	printList(res)
	print ("")

	arr1 = [0]
	LL1 = LinkedList()
	for i in arr1:
		LL1.insert(i)
	print("First list is", end = " ")
	printList(LL1.head)

	arr2 = [0]
	LL2 = LinkedList()
	for i in arr2:
		LL2.insert(i)
	print("Second list is", end = " ")
	printList(LL2.head)

	# Function Call
	res = AddTwoNumbers().addTwoNumbers(LL1.head, LL2.head)
	print("Resultant list is", end = " ")
	printList(res)
	print ("")

	arr1 = [9,9,9,9,9,9,9]
	LL1 = LinkedList()
	for i in arr1:
		LL1.insert(i)
	print("First list is", end = " ")
	printList(LL1.head)

	arr2 = [9,9,9,9]
	LL2 = LinkedList()
	for i in arr2:
		LL2.insert(i)
	print("Second list is", end = " ")
	printList(LL2.head)

	# Function Call
	res = AddTwoNumbers().addTwoNumbers(LL1.head, LL2.head)
	print("Resultant list is", end = " ")
	printList(res)
	print ("")

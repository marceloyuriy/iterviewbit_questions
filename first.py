'''
In this archive, i'll write the code of some basics structures, algorithms, and variables manipulations.

'''

#Linked List Structure

# Node class
class Node:
    # Function to initialize the node object
    def __init__(self, v):
        self.val = v  # Assign value
        self.next = None  # Initialize next as null
  
# Linked List class
class ListNode:
    # Function to initialize the Linked List
    def __init__(self): 
        self.head = None
        
#Sort Binary Linked List (Amazon)
        
class solution:
    def solve (self, A):
        #Case of empty linked list
        if A == None:
            return
        start = A
        count1 = 0
        count0 = 0
        while not A == None:
            if A.val == 1:
                count1 = count1 + 1
            else:
                count0 = count0 + 1
            A = A.next
        A = start 
        while not A == None: 
            if count0 > 0:
                A.val = 0
                count0 = count0 - 1
            else: 
                A.val = 1
                count1 = count1 - 1
            A = A.next
        A = start
        return A
    
#Remove Duplicates from Sorted List
class Solution:
	# @param A : head node of linked list
	# @return the head node in the linked list
	def deleteDuplicates(self, A): 
            if A == None:
                return None
            start = A
            while not A == None: 
                if A.next.val == A.val:
                    A.next = A.next.next
                else: 
                    A = A.next
            return start
        
        

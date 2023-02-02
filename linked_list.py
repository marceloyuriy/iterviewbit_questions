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
    
#Remove Duplicates from Sorted List (Amazon)
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
        
#Swap List Nodes in pairs (Amazon)
class Solution:
	# @param A : head node of linked list
	# @return the head node in the linked list
	def swapPairs(self, A):
        dummy = ListNode(0)
        dummy.next = A
        
        prev = dummy
        curr = dummy.next
        while curr and curr.next:
            tmp = curr.next.next
            prev.next = curr.next
            curr.next.next = curr
            curr.next = tmp
            prev = curr
            curr = curr.next
        return dummy.next

#Kth Node From Middle
class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        #Empty linked list
        if A == None:
            return -1
        start = A
        number_nodes = 1
        #Finding the number of Nodes
        while A:
            number_nodes = number_nodes + 1
            A = A.next
        #Finding the middle node
        middle = number_nodes//2 + 1
        kth_number = middle - B
        if kth_number > 0:
            count = 1
            kth = start
            while count < kth_number:
                kth = kth.next
                count = count + 1
            return kth.val
        else: 
            return -1
#List Cycle
class Solution:
    # @param A : head node of linked list
    # @return the first node in the cycle in the linked list
    def detectCycle(self, A):
        #Empty linked list
        if A == None:
            return None
        #This solution uses a function set(), which is a collection of non-repetibles items. Here, it will be use as a hash map
        #Considering that all entries are different
        '''
        The functions that can be use in set() are the following: 
            add() 
            remove()
            len()
        '''
        seen = set()
        while A:
            if A.val in seen:
                return A.val
            else: 
                seen.add(A.val)
                A = A.next
        
            
            

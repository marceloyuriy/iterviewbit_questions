'''Kth Smallest Element In Tree
Given a binary search tree, write a function to find the kth smallest element in the tree.
NOTE: You may assume 1 <= k <= Total number of nodes in BST
'''
# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
	# @param A : root node of tree
	# @param B : integer
	# @return an integer
	def inOrder(self, A, B, lis):
        if (A==None):
            return
        if (len(lis)>=B):
            return
        self.inOrder(A.left,B,lis)
        lis.append(A.val)
        self.inOrder(A.right,B,lis)
    def kthsmallest(self, A, B):
        lis=[]
        self.inOrder(A,B,lis)
        return lis[B-1]
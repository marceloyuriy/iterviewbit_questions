'''
#Implementation of heap sort in python:
def heapsort(A):
   build_max_heap(A)
   for i in range(len(A) - 1, 0, -1):
       A[0], A[i] = A[i], A[0]
       max_heapify(A, index=0, size=i)
def parent(i):
   return (i - 1)//2
def left(i):
   return 2*i + 1
def right(i):
   return 2*i + 2
def build_max_heap(A):
   length = len(A)
   start = parent(length - 1)
   while start >= 0:
       max_heapify(A, index=start, size=length)
       start = start - 1
def max_heapify(A, index, size):
   left_child = left(index)
   right_child = right(index)
   if (left_child < size and A[left_child] > A[index]):
       largest = left_child
   else:
       largest = index
   if (right_child < size and A[right_child] > A[largest]):
       largest = right_child;
   if (largest != index):
       A[largest], A[index] = A[index], A[largest]
       max_heapify(A, largest, size)
A = input('Enter the list of numbers: ').split()
A = [int(x) for x in A]
heapsort(A)
print('Sorted list: ', end='')
print(A)
'''

'''K Largest Elements
Given an 1D integer array A of size N you have to find and return the B largest elements of the array A.

NOTE:

Return the largest B elements in any order you like.

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def solve(self, A, B):

    
        #Functions to create a max heap
        def heapsort(A):
           build_max_heap(A)
           for i in range(len(A) - 1, 0, -1):
               A[0], A[i] = A[i], A[0]
               max_heapify(A, index=0, size=i)
        def parent(i):
           return (i - 1)//2
       
        def left(i):
           return 2*i + 1
       
        def right(i):
           return 2*i + 2
       
        def build_max_heap(A):
           length = len(A)
           start = parent(length - 1)
           while start >= 0:
               max_heapify(A, index=start, size=length)
               start = start - 1
               
        def max_heapify(A, index, size):
           left_child = left(index)
           right_child = right(index)
           if (left_child < size and A[left_child] > A[index]):
               largest = left_child
           else:
               largest = index
           if (right_child < size and A[right_child] > A[largest]):
               largest = right_child;
           if (largest != index):
               A[largest], A[index] = A[index], A[largest]
               max_heapify(A, largest, size)
        ans = {}
        for i in range(B):
            ans[A[i]] = 1
        return ans
               
        

               
A = [ 56, 56, 34, 34, 72, 71 ]
B = 5
ans = Solution.solve(A,A,B)
print (ans) 
'''
'''Distinct Numbers in Window
You are given an array of N integers, A1, A2 ,..., AN and an integer B. Return the of count of distinct numbers in all windows of size B.

Formally, return an array of size N-B+1 where i'th element in this array contains number of distinct elements in sequence Ai, Ai+1 ,..., Ai+B-1.

NOTE:  if B > N, return an empty array.
'''
class Solution:
	# @param A : list of integers
	# @param B : integer
	# @return a list of integers
	def dNums(self, A, B):
         cnt=0
	     dct = {}
         for i in range(B):
             if A[i] in dct:
                 dct[A[i]]+=1
             else:
                 dct[A[i]]=1
                 cnt+=1
         ans=[cnt]
         for i in range(B,len(A)):
             if A[i] in dct:
                 if dct[A[i]]==0:
                     cnt+=1
                 dct[A[i]]+=1
             else:
                 dct[A[i]]=1
                 cnt+=1
             if dct[A[i-B]]==1:
                 cnt-=1
             dct[A[i-B]]-=1
             ans.append(cnt)
         return ans
     
A = [1, 2, 1, 3, 4, 3]
B = 3
ans = Solution.dNums(A,A,B)
print (ans)

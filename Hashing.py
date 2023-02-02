'''Dictionary
Declaration :
    A = {}
Adding an key, value pair :
    A[key] = value // O(1) average time. O(n) worst case
Find the value for key = K:
    A[K] // O(1) average, O(n) worst
Size ( number of elements ) of the vector :
    len(A) // O(1) 
Erase from the map :
    del A[K] // O(1) average, O(n) worst
'''

'''
#First Repeating element
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        n = len(A)
        # Initialize index of first repeating element
        mini = -1
    
        # Creates an empty hashset named ump
        ump = {}
    
        # Traverse the input array from right to left
        for i in range(n-1, -1, -1):
            # If element is already in hash set, update min
            if ump.get(A[i]) != None:
                mini = i
            else:   # Else add element to hash set
                ump[A[i]] = 1
        print (ump)
        if(mini == -1):
            return mini
        
        return A[mini]

#    0   1  2  3  4  5  6
A = [10, 5, 3, 4, 3, 5, 6]
ans = Solution.solve(A,A)
print (ans)
'''

'''
#2sum
class Solution:
	# @param A : tuple of integers
	# @param B : integer (Target)
	# @return a list of integers [index1, index2]
	def twoSum(self, A, B):
        hmap = {} #Hash map of intergers in A
        #Create a hashmap of values and their index
        for i in range(len(A)):
            diff = B - A[i]
            if not hmap.get(diff):
                hmap [A[i]] = i
            else: 
                index1 = hmap.get(diff)
                index2 = i
                ans = [index1, index2]
        return ans
                
A = [2, 7, 11, 15]
B = 9
ans = Solution.solve(A,A,B)
print (ans)
'''

'''Anagrams
Given an array of strings, return all groups of strings that are anagrams. Represent a group by a list of integers representing the index in the original list. Look at the sample case for clarification.

Anagram : a word, phrase, or name formed by rearranging the letters of another, such as 'spar', formed from 'rasp'

Note:  All inputs will be in lower-case.

Example :

Input : cat dog god tca
Output : [[1, 4], [2, 3]]
cat and tca are anagrams which correspond to index 1 and 4. 

dog and god are another set of anagrams which correspond to index 2 and 3.

The indices are 1 based ( the first element has index 1 instead of index 0).

Ordering of the result : You should not change the relative ordering of the words / phrases within the group. Within a group containing A[i] and A[j], A[i] comes before A[j] if i < j.

from collections import defaultdict
class Solution:
	# @param A : tuple of strings
	# @return a list of list of integers
	def anagrams(self, A):
          hash_map = defaultdict(list)
          i = 1
          for word in A:
              count = [0] * 26 #a ... z = total of 26 characters
              for char in word:
                  count[ord(char) - ord('a')] += 1 #ord mean ASCII value
            
              hash_map[tuple(count)].append(i)
              i += 1
            
          return list(hash_map.values())

A = ("cat", "dog", "god", "tca")   
ans = Solution.anagrams(A,A)
print (ans)  
'''  

'''Check Palindrome!
Given a string A consisting of lowercase characters.

Check if characters of the given string can be rearranged to form a palindrome.

Return 1 if it is possible to rearrange the characters of the string A such that it becomes a palindrome else return 0.

from collections import defaultdict
class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        #Build a hash map of each letter
        hmap = defaultdict(list)
        for i in range(len(A)): 
            hmap[A[i]].append(i)
        print(hmap)
        for c in A: 
            if len(hmap[c])%2 != 0: 
            return 1
        else:
            return 0

A = "vnpypznzpfxyivpppxfpp"   
ans = Solution.solve(A,A)
print (ans)  
'''

'''Two out of Three
Given are Three arrays A, B and C.

Return the sorted list of numbers that are present in atleast 2 out of the 3 arrays.

class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @param C : list of integers
    # @return a list of integers
    def solve(self, A, B, C):
        hashmap = {}
        hash_ans = {}
        ans = []
        for i in A: 
            hashmap[i] = 1
        for i in B:
            if i in hashmap:
                hash_ans[i] = 1
            else:
                hashmap[i] = 1
        for i in C:
            if i in hashmap:
                hash_ans[i] = 1
            else:
                hashmap[i] = 1
        for i in hash_ans:
            ans.append(i)
        ans.sort()
        return ans
        
A = [ 56, 56, 34, 34, 72, 71 ]
B = [ 56, 56, 34, 34, 72, 71 ]
C = [ 56, 56, 34, 34, 72, 71 ]
ans = Solution.solve(A,A,B,C)
print (ans) 
'''

'''Longest Substring Without Repeat
Given a string, 

find the length of the longest substring without repeating characters.

Example:

The longest substring without repeating letters for "abcabcbb" is "abc", which the length is 3.

For "bbbbb" the longest substring is "b", with the length of 1.
'''
class Solution:
	# @param A : string
	# @return an integer
	def lengthOfLongestSubstring(self, A):
         hashmap = {}
         max_len = 0
         len_substr = 0
         for c in A:
             if not c in hashmap:
                 hashmap[c] = 1 
                 len_substr += 1
             else: 
                 len_substr = 1
             if len_substr > max_len:
                 max_len = len_substr
         return max_len
     
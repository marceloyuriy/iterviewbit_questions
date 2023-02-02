'''Stacks
Stack declaration:
    A = [] # declares an empty stack. O(1)
Push
    A.append(newElement) # Put the new Element on the end of the array. O(1).
Pop
    A.pop()  # removes the last element. O(1)
isEmpty
    return (len(A) == 0); # Check if size is 0. O(1)
Size
    return len(A); # O(1)  
Top
    A[-1] # O(1)



'''

'''Queues
Queue declaration :
     A = deque() # declares an empty queue. O(1)
Push
    A.append(newElement) # Put the new Element on the end of the array. O(1).
Pop
    A.popleft() # Pops out the front of the queue
isEmpty
    return (len(A) == 0); # Check if size is 0. O(1)
Size
    return len(A); # O(1)  
Front
    A[0] # O(1)
'''

#Balanced Parantheses!
class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        left_bracket = []
        for x in A:
            if x == '(':
                left_bracket.append(x)
            else: 
                if len(left_bracket) > 0:
                    left_bracket.pop()
                else: 
                    return 0
        if len(left_bracket) == 0:
            return 1
        else:
            return 0
    
#Nearest Smaller Element
class Solution:
	# @param A : list of integers
	# @return a list of integers
	def prevSmaller(self, A):
        ans = []
        stack = []
        for i in range(0, len(A), 1): 
            while (stack!=[] and stack[-1]>=A[i]):
                stack.pop()
            if stack == []:
                ans.append(-1)
            else:
                ans.append(stack[- 1])
    
            stack.append(A[i])

        return ans
#First Non-Repeating Character In A Stream Of Characters
class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        #Build a hash map of each letter
        dic = {}
        lowercases = "abcdefghijklmnopqrstuvwxyz"
        for a in lowercases:
            dic[a] = True
        queue = []
        output = ""
        for a in A:
            if a not in queue and dic[a] == True:
                queue.append(a)
            else:
                if a in queue:
                # queue will store only unique values if any value 
                # is repeating in dictionary that value's value will be made False         
                    queue.remove(a)
                dic[a] = False
            if not queue:
                output += "#"
            else:
                output += queue[0]
        return output
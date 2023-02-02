class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def slidingMaximum(self, A, B):
        #Brute force solution
        #Trivial cases
        if len(A) == 0: 
            return []
        if B >= len(A): 
            return [max(A)]
        
        import collections
        window = collections.deque()
        C = []
        for left_pointer in range(0, len(A) - B + 1):
            right_pointer = left_pointer + B - 1
            
            if len(window) == 0:
                for i in range(left_pointer, right_pointer + 1): 
                    window.append(A[i])
            else: 
                window.popleft()
                window.append(A[right_pointer])
            
            C.append(max(window))
        
        return C
        #Time complexity of this algorithm is O(n^2), because the max function has time complexity of O(n)
        
A = [ 10, 9, 8, 7, 6, 5, 4, 3, 2, 1 ]
B = 2
ans = Solution.slidingMaximum(A, A, B)
print(ans)

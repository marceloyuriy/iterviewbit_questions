class Solution:
	# @param A : tuple of integers
	# @param B : tuple of integers
	# @return an integer
	def canCompleteCircuit(self, A, B):
        #A -> Amount of gas
        #B -> Cost of travel
        curr_tank = 0 #Amount of gas in the curr_tank
        
        '''Brute force Solution
        two nested loops, first to change the starting point, and second to go throught array
        Time complexity of O(n^2)
        for i in range(len(A)):
            for pos in range (len(B)):
        ''' 
        #Better solution
        
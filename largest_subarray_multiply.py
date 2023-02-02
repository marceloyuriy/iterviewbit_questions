#Lasgest subarray multiplication
#Here we need to find the subarray that result in the largest result
class Solution: 
    def maxProduct (self, nums):
        res = max(nums)
        curMin, curMax = 1,1
        
        for n in nums: 
            tmp = curMax*n
            curMax = max(n*curMax, n*curMin, n)
            curMin = min(tmp, n*curMin, n)
            res = max(res, curMax, curMin)
        return res
        
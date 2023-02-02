#Longest increasin subsequence
#The approach for this question is use DFS with cache. We start from end of array calculating the
#longest increasing subsequence of last element and saving in DP array. The longest subsequence from next element
#is the max of one, and 1 plus LIS of last element. The process is repeated until the first element. 
#This solution has time complexity of O(N^2). The Brute force solution has time complexity of O(2^N). 
class Solution: 
    def lenghtOfLIS (self, nums): 
        LIS = [1]* (len(nums))
        
        for i in range(len(nums) - 1, -1, -1):
            for j in range (i+1, len(nums)):
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i], 1 + LIS[j])
        return max(LIS)
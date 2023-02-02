class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        #I'll create two arrays, one with the multiplication of left elements, and other with
        #the multiplication of right elements. The result will be the multiplication of left 
        #element with the right element
        
        #Left array [1 .... 1] 
        #This boudaries one are to avoid boundaries conditions
        left_mult_array = [1] * (len(nums) + 1)

        #Right array [1 .... 1]
        right_mult_array = [1] * (len(nums) + 1)

        #Calculating the values of each array
        #left to right
        for index in range(len(nums)): 
            left_mult_array[index+1] = left_mult_array[index] * nums[index]
        
        #right to left
        for index in range(len(nums)-1, -1, -1): 
            right_mult_array[index] = right_mult_array[index + 1] * nums[index]
        
        result = []
        for i in range(len(nums)): 
            curr_value = left_mult_array[i] * right_mult_array[i+1]
            result.append(curr_value)
        
        return result
    

nums = [1,2,3,4]
ans = Solution.productExceptSelf(nums, nums)
print(ans)
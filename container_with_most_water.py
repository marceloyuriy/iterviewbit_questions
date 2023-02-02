class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        N = len(height)
        left, right = 0, N-1
        max_area_water = 0

        while left < right: 
            curr_area = min(height[left], height[right])*(right - left)
            max_area_water = max(curr_area, max_area_water)
            if height[left] < height[right]: 
                left += 1 
            elif height[right] < height[left]: 
                right -= 1
            else: 
                right -= 1

        return max_area_water


height = [1,8,6,2,5,4,8,3,7]
ans = Solution.maxArea(height, height)
print(ans)
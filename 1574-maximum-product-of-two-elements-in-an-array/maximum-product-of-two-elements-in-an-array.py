class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max1 = nums[0]
        max2 = 0
        for i in range(1, len(nums)):
            if max1 < nums[i]:
                max2 = max1
                max1 = nums[i]
            elif max2 < nums[i]:
                max2 = nums[i]
        return ((max1-1)*(max2-1))
                
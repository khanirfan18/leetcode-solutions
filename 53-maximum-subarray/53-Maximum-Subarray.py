class Solution:
    def maxSubArray(self, nums: list[int]) -> int:

        new_total = nums[0]
        total = nums[0]
        for num in nums[1:]:
            if total >= 0:
                total += num
            else:
                total = num

            if total > new_total:
                new_total = total


        return new_total



        


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        temp = [0] * len(nums)
        for i in range(0,len(nums)):
            temp[i] = nums[i]*nums[i]
        temp.sort()


        return temp
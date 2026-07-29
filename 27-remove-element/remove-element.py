class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        hold = 0
        for i in range(0, len(nums)):
            if nums[i] != val:
                nums[hold] = nums[i]
                hold+=1
            
        return hold
                
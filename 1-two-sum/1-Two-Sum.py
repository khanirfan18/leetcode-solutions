class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hash_map = {}
        i = 0
        
        for i in range(len(nums)):
            remain = target - nums[i]

            if remain not in hash_map:
                hash_map[nums[i]] = i
            else:
                return [hash_map[remain], i]

       
            

        
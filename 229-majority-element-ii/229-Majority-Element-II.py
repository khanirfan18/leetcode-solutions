class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        if not nums:
            return []

        count_one = 0
        majority_one = None

        count_two = 0
        majority_two = None

        # same as lc169
        for num in nums:
            if num == majority_one:
                count_one += 1
            elif num == majority_two:
                count_two += 1
            elif count_one == 0:
                majority_one = num
                count_one = 1
            elif count_two == 0:
                majority_two = num
                count_two = 1
            else:
                count_one -= 1
                count_two -= 1
        
        # verif
        freq1 = 0
        freq2 = 0
        n = len(nums)
        
        for num in nums:
            if num == majority_one:
                freq1 += 1
            elif num == majority_two:
                freq2 += 1

        result = []
        if freq1 > n // 3:
            result.append(majority_one)
        if freq2 > n // 3 and majority_two != majority_one:
            result.append(majority_two)
            
        return result
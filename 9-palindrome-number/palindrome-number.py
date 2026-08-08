class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        nums = list(map(int, str(x)))
        i = 0
        j = len(nums) - 1

        while i < j:
            if nums[i] != nums[j]:
                return False
            else:
                i += 1
                j -= 1

        return True
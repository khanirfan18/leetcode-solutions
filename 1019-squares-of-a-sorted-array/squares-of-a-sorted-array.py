class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        temp = []
        for i in nums:
            temp.append(i*i)
        
        temp.sort()

        return temp
            
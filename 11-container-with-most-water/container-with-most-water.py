class Solution:
    def maxArea(self, height: List[int]) -> int:
        # area = width x height
        # width right - left
        maxarea = 0
        right = len(height) - 1
        left = 0
        while left < right:
            tempwidth = right - left
            tempheight = min(height[left], height[right])
            temparea = tempwidth*tempheight
            if temparea > maxarea:
                maxarea = temparea
                
            if height[left] > height[right]:
                right-=1
            else:
                left+=1
            
        return maxarea
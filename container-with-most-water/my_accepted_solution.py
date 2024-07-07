class Solution:
    def maxArea(self, h: List[int]) -> int:
        
        left = 0
        right = len(h) - 1
        maxA = 0

        while left < right:

            if h[left] < h[right]:
                area = (right - left) * h[left]
                left += 1
            else:
                area = (right - left) * h[right]
                right -= 1
            
            if area > maxA:
                maxA = area

        return maxA
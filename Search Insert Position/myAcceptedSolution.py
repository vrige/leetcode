class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        pos = 0 
        n = len(nums)
        for i in range(n):
            if nums[i] == target:
                return i
            if i > 0 and target > nums[i - 1]:
                pos = i
        if target > nums[n - 1]:
            pos = n
        return pos
        
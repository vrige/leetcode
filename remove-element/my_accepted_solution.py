class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        n = len(nums)
        s = n
        for i in range(0,n):
            
            if nums[i] == val:
                s -= 1
                nums[i] = float('inf')
            
        nums.sort()
        
        return s

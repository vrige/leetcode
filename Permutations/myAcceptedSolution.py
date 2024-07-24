class Solution:
    def __init__(self):
        self.s = []

    def permute(self, nums: List[int]) -> List[List[int]]:
        
        n = len(nums)
        for i,val in enumerate(nums):
            used = []
            used.append(val)
            self.recursive(nums[:i] + nums[i+1:], used, n -1)
        
        return self.s

    def recursive(self, nums, nums_2, l):
        free = nums.copy()
        used = nums_2.copy()

        if l > 1:
            for i, val in enumerate(free):
                self.recursive(free[:i] + free[i+1:], used + [val], l - 1)
        else:
            self.s.append(used + free)

            
    

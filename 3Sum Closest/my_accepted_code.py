class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        n = len(nums)
       
        dist = float('inf')
        nums.sort()
        ret_sum = float('inf')

        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            i1 = i + 1
            i2 = n - 1
            while i1 < i2:
                summ = nums[i] + nums[i1] + nums[i2]
                s = summ - target
                if s == 0:
                    return summ
                elif s < 0:
                    i1 += 1
                    
                    while i1 < i2 and nums[i1] == nums[i1-1]:
                        i1 += 1
                elif s > 0:
                    i2 -= 1
                    while i1 < i2 and nums[i2] == nums[i2+1]:
                        i2 -= 1
                if dist > abs(s): 
                    dist = min(dist, abs(s))
                    ret_sum = summ

        return ret_sum
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        nums.sort()
        n = len(nums)
        out = []
        mapping = []
        if n >= 4:
            for i in range(n-3):
                for j in range(i+1,n-2):
                    
                    if j > i+1 and nums[j] == nums[j-1] and j != n-3:
                        if nums[i] == nums[j]:
                            break
                        continue
                    
                    l = j + 1
                    r = n - 1

                    while l < r:
                        summ = nums[i] + nums[j] + nums[l] + nums[r]
                        s = summ - target

                        if s == 0:
                            if (nums[i], nums[j], nums[l], nums[r]) not in mapping:
                                mapping.append((nums[i], nums[j], nums[l], nums[r]))
                                out.append([nums[i], nums[j], nums[l], nums[r]])
                            l += 1
                            r -= 1
                        elif s < 0:
                            l += 1
                            
                        else:
                            r -= 1
                            
        return out
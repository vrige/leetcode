class Solution:
    def jump(self, nums: List[int]) -> int:
        
        end = len(nums) - 1
        min_i = end
        output = 0

        while end > 0:

            for i in range(end):

                for v in range(nums[i]+1):
                   
                    if i + v == end and min_i > i:
                        min_i = i

            if min_i != end:
                output += 1
                end = min_i

        return output

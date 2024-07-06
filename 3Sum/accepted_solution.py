class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums = self.mergeSort(nums)
        output = []
        n = len(nums)
        
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue 
            
            if nums[i] > 0:
                break 
            
            left, right = i + 1, n - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    output.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    # Skip duplicates for the second and third elements
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1
        
        return output

    def mergeSort(self, nums: List[int]) -> List[int]:
        if len(nums) < 2:
            return nums
            
        midpoint = len(nums) // 2

        return self.merge(self.mergeSort(nums[:midpoint]), self.mergeSort(nums[midpoint:]))


    def merge(self, num_left, num_right):
        if not num_left:
            return num_right

        if not num_right:
            return num_left

        result = []
        index_left = index_right = 0

        while len(result) < len(num_left) + len(num_right):

            if num_left[index_left] <= num_right[index_right]:
                result.append(num_left[index_left])
                index_left += 1
            else:
                result.append(num_right[index_right])
                index_right += 1

            if len(num_left) == index_left:
                result += num_right[index_right:]
                break

            if len(num_right) == index_right:
                result += num_left[index_left:]
                break
            
        return result
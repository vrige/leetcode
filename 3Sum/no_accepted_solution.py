class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        output = []
        hashh = []
        nums = self.mergeSort(nums)
        lenn = len(nums)
        print(nums)

        for i, num in enumerate(nums):

            if num > 0:
                break
            
            y = lenn - 1
            
            while i < y:

                x = nums[y]
                var = -num - x
                if {num, x, var} not in hashh and var in nums[i+1:y]:
                    hashh.append({num, x, var})  
                    output.append([num, x, var])
                y -= 1
        
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
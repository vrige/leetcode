class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if nums and len(nums) >= 2 and len(nums) <= pow(10,4) and target <= pow(10,9) and target >= -pow(10,9):
            origin_num = nums.copy()

            # remove all the nums > target
            for num in nums: 
                if num > pow(10,9) or num < -pow(10,9):
                    nums.remove(num)
            
            if not nums:
                return []
            
            # sort the nums with Merge Sort
            ord_nums = self.mergeSort(nums)

            for i, x in enumerate(ord_nums[:(len(ord_nums)-1)]):
                for j, y in enumerate(ord_nums[(i+1):]):
                    if x + y == target:
                        return self.elab_sol(origin_num, [x,y])
                    if x + y > target:
                        break

        return []

    def elab_sol(self, nums: List[int], nums_ord: List[int]) -> List[int]:
        try:
            c = []
            if nums_ord[0] != nums_ord[1]:
                c += [nums.index(nums_ord[0]), nums.index(nums_ord[1])]
            else:
                a = nums.index(nums_ord[0])
                nums.remove(nums_ord[0])
                c +=  [a, nums.index(nums_ord[1])+1]
            return self.mergeSort(c)
        except ValueError as e:
            print(f"Error: {e}")
            return []

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
class Solution:
    solution: List[List[int]] = []
    
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.solution = []
        for i, val in enumerate(candidates):
            self.summ(candidates,target,val,[val],i)
        return self.solution
    
    def summ(self, candidates: List[int], target: int, sum: int, list_c: List[int], index: int):
        if sum > target:
            pass
        elif sum == target:
            self.solution.append(list_c)
        else:
            same = candidates[index]
            self.summ(candidates, target, sum+same, list_c+[same], index)

            for ind in range(index + 1, len(candidates)):      
                next = candidates[ind]
                self.summ(candidates, target, sum+next, list_c+[next], ind)

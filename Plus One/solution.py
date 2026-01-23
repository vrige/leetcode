class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        output = str(sum([v * pow(10, i) for i, v in enumerate(reversed(digits))]) + 1)
        return [int(s) for s in output]
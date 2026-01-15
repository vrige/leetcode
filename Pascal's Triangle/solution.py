class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        input = [1,1]
        output = [[1]]
        for i in range(numRows-1):
            output.append(input)
            input = self.traverse(input)
        return output

    def traverse(self, input: List[int]) -> List[int]:
        output = [1]
        for i in range(len(input)):
            j = i + 1
            if i >= len(input) or j >= len(input):
                break
            output.append(input[i] + input[j])
        output.append(1)
        return output
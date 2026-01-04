class Solution:
    soll: List[List[str]] = []

    def solveNQueens(self, n: int) -> List[List[str]]:
        self.soll = []
        if n <= 0:
            return []
        for s in range(n):
            output = self.solveNQueensWithHint(n, [s])
        return self.soll

    def solveNQueensWithHint(self, n: int, s: List[int]):
        if n == len(s):
            self.soll.append(self.transformedList(s))

        diag = []
        step = len(s)
        for ordd, value in enumerate(s):
            diag_d = value + (step - ordd) 
            diag_u = value - (step - ordd)
            if diag_d < n and diag_d >= 0:
                diag.append(diag_d)
            if diag_u < n and diag_u >= 0: 
                diag.append(diag_u)

        for step_c in range(n):
            if step_c in s or step_c in diag:
                continue
            else:
                output = self.solveNQueensWithHint(n, s + [step_c])
    
    def transformedList(self, s: List[int]):
        n = len(s)
        output = []
        for step in s:
            temp = "."*n
            temp = temp[:step] + "Q" + temp[step+1:]
            output.append(temp)
        return output

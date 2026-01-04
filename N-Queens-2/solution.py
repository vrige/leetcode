class Solution:
    sol: int = 0

    def totalNQueens(self, n: int) -> int:
        self.sol = 0
        if n <= 0:
            return 0
        for s in range(n):
            output = self.solveNQueensWithHint(n, [s])
        return self.sol

    def solveNQueensWithHint(self, n: int, s: List[int]):
        if n == len(s):
            self.sol += 1

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
   
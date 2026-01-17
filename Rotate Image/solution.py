class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        levels = n // 2

        for lev in range(levels):
            internal = n - 1 - (2 * lev)
            for i in range(internal):
                temp = (i+lev,0+lev)
                prev = self.rot_r(temp[0], temp[1])
                for j in range(3):
                    matrix[temp[0]][temp[1]], matrix[prev[0]][prev[1]] = matrix[prev[0]][prev[1]], matrix[temp[0]][temp[1]]
                    temp = self.rot_r(temp[0], temp[1])
                    prev = self.rot_r(temp[0], temp[1]) 

    def rot_r(self, x, y):
        return -(y+1), x

    def rot_l(self, x, y):
        return y, -(x+1)

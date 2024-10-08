class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        i = 0
        j = 0
        while i <= 8 and j <= 8:

            temp = board[i][j]
            if temp != ".":
                
                if board[i].index(temp) != j:
                    return False

                for l in range(9):
                    if l == i:
                        continue
                    if temp == board[l][j]:
                        return False

                for l in range(9):
                    posX = (i//3) * 3 + l//3
                    posY = (j//3) * 3 + l % 3
                    if posX == i and posY == j:
                        continue
                    if board[posX][posY] == temp:
                        return False

            if i != 8:
                i += 1
            else:
                j += 1
                i = 0
    
        return True
            
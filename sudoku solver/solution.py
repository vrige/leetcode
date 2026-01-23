import copy

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        nums = {"1","2","3","4","5","6","7","8","9"}

        # Init possibility and quads matrix
        possible_s = {}
        quads = {}
        colss = {}
        for row_n, row in enumerate(board):
            if "." not in row:
                continue
            for j, v in enumerate(row):
                if v == ".":
                    x = row_n
                    y = j
                    row_p = nums - set(board[x])
                    col = []
                    if y not in colss:
                        col = [i[y] for i in board if i[y] != "."]
                    else:
                        col = colss[y]
                    col_p = row_p - set(col)

                    v_quad = (y // 3 ) 
                    h_quad = (x // 3 )
                    quad = []
                    if (h_quad, v_quad) not in quads:
                        vv = v_quad * 3
                        hh = h_quad * 3
                        v_quad_l = [vv, vv+1, vv+2]
                        h_quad_l = [hh, hh+1, hh+2]
                        for i in h_quad_l:
                            for j in v_quad_l:
                                ele = board[i][j]
                                if ele != ".":
                                    quad.append(ele)
                    else:
                        quad = quads[(h_quad, v_quad)]
                    possib = col_p - set(quad)

                    possible_s.update({(x,y): possib})
                    quads.update({(h_quad, v_quad): set(quad)})
                    colss.update({y: set(col)})

        
        # Order the starting matricies
        possible_s = dict(sorted(possible_s.items(), key=lambda item: len(item[1])))
        new_possible_s = {k: v.copy() for k, v in possible_s.items()}
        new_board = [row[:] for row in board]

        # Start backtracking
        start = list(new_possible_s)[0]
        output = []
        sol = []
        for chosen in new_possible_s[start]:
            output = self.solve(sol, new_possible_s, start, chosen)
            if output != -1:
                return self.update_sodoku(board, sol)
        return -1
        
    def update_sodoku(self, board, sol):
        for move in sol:
            for (x,y), val in move.items():  # iterate the key-value pair
                board[x][y] = val
        return board
        
    def solve(self, sol, possible_s, start, chosen):

            new_possible_s = {k: v.copy() for k, v in possible_s.items()}
            
            x = start[0]
            y = start[1]
            v = {chosen}
            v_quad = (y // 3) 
            h_quad = (x // 3)
            possibilities = new_possible_s[(x,y)]
            
            for pos_, v_ in list(new_possible_s.items()):
                v_quad_ = (pos_[1] // 3) 
                h_quad_ = (pos_[0] // 3)
                if pos_[0] == x and pos_[1] == y:
                    continue
                if pos_[0] == x or pos_[1] == y or (h_quad, v_quad) == (h_quad_, v_quad_):
                    v_ = v_ - v
                    if not v_:
                        sol.pop()
                        return -1
                    new_possible_s.update({pos_: v_})

            # Change is ok in looktable + 1
            if (x,y) in new_possible_s:
               del new_possible_s[(x,y)]

            # Order
            new_possible_s = dict(sorted(new_possible_s.items(), key=lambda item: len(item[1])))
            sol.append({(x,y): chosen})

            # Next if there is
            if not new_possible_s:
                return sol
            next_ = list(new_possible_s)[0]
            output = []
            for i in new_possible_s[next_]:
                output = self.solve(sol, new_possible_s, next_, i)
                if output != -1:
                    return output
            return -1
            


                
        

                
from typing import Optional

class Solution:
    # def knights_tour(self, n) -> Optional[list(list(int))]:
    def knights_tour(self, n):
        moves = [(1,2), (-1,2), (1,-2), (-1,-2),
                 (2,1), (-2,1), (2,-1), (-2,-1)]
        
        board = [[None]*n for _ in range(n)]

        def is_safe(r, c):
            if r<0 or r>n-1 or c<0 or c>n-1:
                return False
            if board[r][c] is not None:
                return False
            return True

        def gen(r, c, count):
            # print(f"r:{r}, c:{c}")
            if count == (n*n):
                return True
            
            # print("--------------------")
            # for row in board_r:
            #     print(f"\t{row}")
            # print("--------------------")    
            
            if is_safe(r,c):
                for (x,y) in moves:
                    # do
                    board[r][c]=count

                    #op
                    if gen(r+x, c+y, count+1):
                        return True
                    
                    # undo
                    board[r][c]=None
            return False
        
        is_valid = gen(0, 0, 0)

        if is_valid:
            return board
        else:
            return -1

if __name__ == '__main__':
    solve = Solution()
    
    sol = solve.knights_tour(7)
    if sol!=-1:
        print("#####################")
        for row in sol:
            print(f"\t{row}")
        print("#####################")
    else:
        print(-1)
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols = len(board), len(board[0])

        def dfs(r,c):
            if (r<0 or r>=rows or c<0 or c>=cols or board[r][c]!='O'):
                return
            board[r][c] = 'T'
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
        
        for r in range(rows):
            for c in range(cols):
                if ( board[r][c]== 'O' and  (r in [0,rows -1] or c in [0, cols-1]) ):
                    dfs(r,c)
        # replace all O with X
        for i in range(rows):
            for j in range(cols):
                if board[i][j]=='O':
                    board[i][j] = 'X'
        
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'T':
                    board[i][j] = 'O'
        

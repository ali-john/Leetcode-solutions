class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return 
        rows,cols = len(board), len(board[0])
        visited = set()

        
        def bfs(r,c):
            q = []
            q.append((r,c))
            visited.add((r,c))
            board[r][c] = "T"
            directions = [[1,0],[-1,0],[0,1],[0,-1]]
            while q:
                r,c = q.pop(0)
                for dx,dy in directions:
                    row, col = r+dx, c+dy
                    if row in range(rows) and col in range(cols) and board[row][col]=="O" and (row,col) not in visited:
                        q.append((row,col))
                        visited.add((row,col))
                        board[row][col] = "T"
        for r in range(rows):
            for c in range(cols):
                if r==0 or r==rows-1 or c==0 or c==cols-1: # boundary condition
                    if board[r][c] == "O":
                        bfs(r,c) # mark all connected components as T

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "T":
                    board[r][c] = "O"        

                
        return



        

        

        
            
    
        
        
        




        

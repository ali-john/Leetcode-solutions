class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        neighbours = [[1,0],[-1,0], [0,1],[0,-1], [1,1], [-1,-1], [-1,1], [1,-1]]
        live = set()
        dead = set()

        def is_valid(i,j):
            return ( 0 <= i < m and 0 <= j < n)
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == 1:
                    live.add((i,j))
                else:
                    dead.add((i,j))
        
        # update live:
        # -1 --> DEAD

        for i, j in live:
            nei = 0
            for x,y in neighbours:
                new_i, new_j = i + x, j+ y
                if is_valid(new_i,new_j) and abs(board[new_i][new_j]) == 1:
                    nei+=1
            if nei < 2 or nei > 3:
                board[i][j] = -1
            elif nei == 2 or nei ==3:
                continue

        # update dead cells
        for i, j in dead:
            nei = 0
            for x,y in neighbours:
                new_i, new_j = i + x, j+ y
                if is_valid(new_i,new_j) and abs(board[new_i][new_j]) == 1:
                    nei+=1
            if nei ==3:
                board[i][j] = -2
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == -1:
                    board[i][j] = 0
                elif board[i][j] == -2:
                    board[i][j] = 1
            
        






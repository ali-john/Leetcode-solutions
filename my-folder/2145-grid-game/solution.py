class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        m = len(grid[0])
        new_grid = [[0]*m for _ in range(2)]

        for i in range(2):
            for j in range(m):
                new_grid[i][j] = grid[i][j]
        
        for i in range(1,m):
            new_grid[0][i] = new_grid[0][i-1] + new_grid[0][i]
            new_grid[1][i] = new_grid[1][i-1] + new_grid[1][i]
        
        res = float('inf')
        for i in range(m):
            top = new_grid[0][-1] - new_grid[0][i]
            bottom = new_grid[1][i-1] if i>0 else 0
            robot2 = max(top,bottom)
            res = min(res,robot2)
        return res
            

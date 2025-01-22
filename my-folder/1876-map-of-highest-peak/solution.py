class Solution:
    def highestPeak(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        m = len(grid[0])

        new_grid = [[0]*m for _ in range(n)]
        q = []
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    q.append((i,j,0))
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        
        while q:
            x,y,level = q.pop(0)
            for direction in directions:
                new_x = x + direction[0]
                new_y = y + direction[1]
                if new_x>=0 and new_x<n and new_y>=0 and new_y<m and new_grid[new_x][new_y]==0:
                    new_grid[new_x][new_y] = level+1
                    q.append((new_x,new_y,level+1))
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    new_grid[i][j] = 0
        return new_grid




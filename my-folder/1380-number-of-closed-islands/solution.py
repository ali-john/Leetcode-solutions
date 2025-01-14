class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        def dfs(i,j,visited):
            if i<0 or i>=rows or j<0 or j>=cols or grid[i][j]!=0:
                return
            grid[i][j] = 'T'
            visited.add((i,j))
            directions = [[1,0],[-1,0],[0,1],[0,-1]]
            for direction in directions:
                new_x = i + direction[0]
                new_y = j + direction[1]
                if ((new_x,new_y) not in visited):
                    dfs(new_x,new_y,visited)
        
        # mark all border's ( 0 and connected ) as 'T'
        for i in range(rows):
            for j in range(cols):
                if (i in [0,rows-1] or j in [0,cols -1]) and grid[i][j]==0:
                    visited = set()
                    visited.add((i,j))
                    dfs(i,j,visited)
        
        count = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==0:
                    count+=1
                    visited = set()
                    visited.add((i,j))
                    dfs(i,j,visited)
        return count




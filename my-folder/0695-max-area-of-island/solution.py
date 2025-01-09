class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        def dfs(i,j,visited):
            if i<0 or i>=rows or j<0 or j>=cols or grid[i][j]!=1:
                return 0
            directions = [[1,0],[-1,0],[0,1],[0,-1]]
            visited.add((i,j))
            
            if grid[i][j] ==1:
                grid[i][j] = 'T'
            
            count = 1
            for direction in directions:
                new_i = i + direction[0]
                new_j = j + direction[1]
                if (new_i,new_j) not in visited:
                    count+= dfs(new_i,new_j,visited)
  
            return count
        
        ans = 0
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    ans = max(ans,dfs(r,c,set()))
        return ans

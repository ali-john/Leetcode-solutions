class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])

        def dfs(i,j,visited):
            if i<0 or i>=rows or j<0 or j>=cols or grid[i][j]!='1':
                return
            
            grid[i][j] = 'T'
            visited.add((i,j))
            directions = [[1,0],[-1,0],[0,-1],[0,1]]
            for direction in directions:
                new_i = i + direction[0]
                new_j = j + direction[1]
                if (new_i,new_j) not in visited:
                    dfs(new_i,new_j,visited)
            return 

        count = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=='1': 
                    dfs(r,c,set())
                    count+=1
        return count
        

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows,cols = len(grid), len(grid[0])
        visited = set()
        islands = 0
    
        def bfs(r,c):
            q = []
            q.append((r,c))
            visited.add((r,c))
            while q:
                row,col = q.pop(0)
                directions = [[1,0],[-1,0],[0,1],[0,-1]]
                for dx,dy in directions:
                    r,c = row+dx, col+dy
                    if (r in range(rows) and c in range(cols) and grid[r][c]=="1" and (r,c) not in visited):
                        visited.add((r,c))
                        q.append((r,c))
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]=="1" and (i,j) not in visited:
                    islands+=1
                    visited.add((i,j))
                    bfs(i,j)
        return islands






        

        

class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        rows1, cols1 = len(grid), len(grid[0])
        rows2, cols2 = 3*rows1, 3*cols1
        grid2 = [[0]*cols2 for _ in range(rows2)]

        for i in range(rows1):
            for j in range(cols1):
                r2, c2 = i*3, j*3
                if grid[i][j]=='/':
                    grid2[r2][c2+2] = 1
                    grid2[r2+1][c2+1] = 1
                    grid2[r2+2][c2] = 1
                elif grid[i][j] == '\\':
                    grid2[r2][c2] = 1
                    grid2[r2+1][c2+1] = 1
                    grid2[r2+2][c2+2] = 1
        def dfs(r,c,visited):
            if (r<0 or r==rows2 or c<0 or c==cols2 or grid2[r][c]!=0 or (r,c) in visited):
                return 
            visited.add((r,c))
            nei = [[r+1,c],[r-1,c],[r,c+1],[r,c-1]]
            for nr,nc in nei:
                dfs(nr,nc,visited)        

        res= 0
        visited = set()
        for i in range(rows2):
            for j in range(cols2):
                if grid2[i][j]==0 and (i,j) not in visited:
                    dfs(i,j,visited)
                    res+=1
        return res


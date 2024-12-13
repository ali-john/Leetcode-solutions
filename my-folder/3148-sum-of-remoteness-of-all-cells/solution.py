class Solution:
    def sumRemoteness(self, grid: List[List[int]]) -> int:
        total, result, res = 0, 0, set()
        n = len(grid)
        m = len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j]>0:
                    total+=grid[i][j]
        
        def dfs(i,j):
            q, tot, visited = [(i,j)], 0 ,set()
            visited.add((i,j))

            while q:

                x, y = q.pop()
                tot += grid[x][y]
                for (nx,ny) in [(x+1,y),(x-1,y),(x,y-1),(x,y+1)]:
                    if 0 <= nx < n and 0 <= ny < n and (nx,ny) not in visited and grid[nx][ny] != -1:
                        q.append((nx,ny))
                        visited.add((nx,ny))

            return total - tot, visited
        
        for i in range(n):
            for j in range(m):
                if grid[i][j]!=-1 and (i,j) not in res:
                    x,r  = dfs(i,j)
                    result+= len(r)*x
                    res = res|r
        return result
        
        

            





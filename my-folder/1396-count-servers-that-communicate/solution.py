class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        rows = [0]*n
        cols = [0]*m

        for i in range(n):
            count = 0
            for j in range(m):
                if grid[i][j]:
                    count+=1
            rows[i] = count
                    
        for i in range(m):
            count = 0
            for j in range(n):
                if grid[j][i]:
                    count+=1
            cols[i] = count
        
        ans = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j]:
                    if rows[i]>1 or cols[j]>1:ans+=1
        return ans

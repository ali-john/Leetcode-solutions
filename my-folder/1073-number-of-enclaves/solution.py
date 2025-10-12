class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        visited = [ ['U']*n for _ in range(m)]
        ans = 0

        def dfs(i,j):
            if i < 0 or i >= m or j < 0 or j >= n: return
            if visited[i][j] != 'U': return
            visited[i][j] = 'V'
            for dx, dy in [(0,1), (0,-1), (1,0), (-1,0)]:
                new_x, new_y = i + dx  , j + dy
                if 0 <= new_x < m and 0 <= new_y < n and grid[new_x][new_y] == 1:
                    dfs(new_x, new_y)
            return
                    
        for i in range(m):
            for j in range(n):
                if i == 0 or j ==0 or i == m-1 or j == n-1:
                    if grid[i][j] ==1 and visited[i][j] == 'U':
                        dfs(i,j)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] and visited[i][j] == 'U':
                    ans+=1
        return ans


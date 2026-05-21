class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        n = len(grid2)
        m = len(grid2[0])
        
        def dfs(i,j):
            isSubIsland = (grid1[i][j] == 1)
            grid2[i][j] = -1
            coordinates = [(1,0), (-1,0), (0,-1), (0,1)]
            for dx, dy in coordinates:
                new_x = i + dx
                new_y = dy + j
                if new_x >=0 and new_x < n and new_y >=0 and new_y < m and grid2[new_x][new_y] == 1:
                    isSubIsland &= dfs(new_x, new_y)
            return isSubIsland
        ans = 0
        for i in range(n):
            for j in range(m):
                if grid2[i][j] == 1:
                    if dfs(i,j):
                        ans+=1
        return ans



            



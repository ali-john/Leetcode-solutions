class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        directions = {1: [(0,-1),(0,1)],
                      2: [(-1,0),(1,0)],
                      3: [(0,-1),(1,0)],
                      4: [(0,1),(1,0)],
                      5: [(0,-1),(-1,0)],
                      6: [(0,1),(-1,0)]}
        
        n = len(grid)
        m = len(grid[0])
        visited = set()
        def dfs(i,j):
            visited.add((i,j))
            if i == n - 1 and j == m - 1: return True
            for direction in directions[ grid[i][j] ]:
                new_i = direction[0] + i
                new_j = direction[1] + j
                if 0 <= new_i < n and 0 <= new_j < m and (new_i,new_j) not in visited and (-direction[0], -direction[1]) in directions[grid[new_i][new_j]]:
                    if dfs(new_i,new_j): 
                        return True
            return False
        
        return dfs(0,0)



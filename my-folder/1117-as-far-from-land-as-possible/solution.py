class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        max_distance = float('-inf')
        n = len(grid)
        q = []
        visited = set()
        for i in range(n):
            for j in range(n):
                if grid[i][j] ==1:
                    q.append((i,j,0))
                    visited.add((i,j))
        if len(q)==0: return -1
        if len(q)==(n*n): return -1
        while q:
            x,y,dist = q.pop(0)
            max_distance = max(max_distance,dist)
            directions = [[1,0],[-1,0],[0,1],[0,-1]]
            for direction in directions:
                new_x = x + direction[0]
                new_y = y + direction[1]
                if new_x>=0 and new_x<n and new_y>=0 and new_y<n:
                    if (new_x,new_y) not in visited:
                        q.append((new_x,new_y,dist+1))
                        visited.add((new_x,new_y))
        return max_distance


        


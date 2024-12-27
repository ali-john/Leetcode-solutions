class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        
        if grid[0][0]==1: return -1

        n = len(grid)
        m = len(grid[0])
        directions = [[1,0], [0,1], [-1,0], [0,-1], [1,1], [-1,-1], [1,-1], [-1,1]]

        q = [[1,0,0]]
        visited = {(0,0)}
        while q:
            dist,x,y = q.pop(0)
            if x==n-1 and y==m-1: return dist

            for dx,dy in directions:
                new_x = x+dx
                new_y = y+dy
                if (new_x,new_y) in visited: continue
                visited.add((new_x,new_y))
                if new_x>=0 and new_x<n and new_y>=0 and new_y<m and grid[new_x][new_y]==0:
                    q.append((dist+1,new_x,new_y))
        return -1

    
        
        # # Dijkstra algorithm solution
        # n = len(grid)
        # m = len(grid[0])
        # heap = [(1,0,0)] # dist, x,y
        # visited = [[float('inf')]*m for _ in range(n)]
        # visited[0][0] = 1
        # while heap:
        #     dist,i,j = heapq.heappop(heap)
        #     directions = [[1,0], [0,1], [-1,0], [0,-1], [1,1], [-1,-1], [1,-1], [-1,1]]

        #     if i==n-1 and j==m-1:
        #         return dist
        #     for dx,dy in directions:
        #         new_x = i+dx
        #         new_y = j+dy
        #         if new_x>=0 and new_x<n and new_y>=0 and new_y<m and grid[new_x][new_y]==0:
        #             new_dist = dist + 1
        #             if new_dist < visited[new_x][new_y]:
        #                 visited[new_x][new_y] = new_dist
        #                 heapq.heappush(heap,(new_dist,new_x,new_y))
        # return -1



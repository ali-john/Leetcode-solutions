class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        start = (-1,-1)
        
        def isValid(x,y):
            return (x>=0 and x<n and y>=0 and y<m)

        for i in range(n):
            for j in range(m):
                if grid[i][j] == '*':
                    start = (i,j)
                    break
            if start!=(-1,-1):
                break
        

        heap = [(0,start)]
        distances = [[float('inf')]*m for _ in range(n)]
        while heap:
            dist, node = heapq.heappop(heap)
            x,y = node[0], node[1]
            if grid[x][y]=='#':
                return dist
            
            directions = [(-1,0),(1,0),(0,1),(0,-1)]
            for direction in directions:
                new_x = x + direction[0]
                new_y = y + direction[1]
                if isValid(new_x, new_y):
                    if grid[new_x][new_y]!='X' and grid[new_x][new_y]!='*':
                        new_dist = dist + 1
                        if new_dist < distances[new_x][new_y]:
                            loc = (new_x,new_y)
                            heapq.heappush(heap,(new_dist,loc))
                            distances[new_x][new_y] = new_dist
        return -1
                        



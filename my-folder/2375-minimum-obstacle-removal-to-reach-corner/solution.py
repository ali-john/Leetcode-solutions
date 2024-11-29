class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        distances = [[float('inf')]*m for _ in range(n)]
        distances[0][0] = 0

        heap = [(0,0,0)] # distance, x,y
    
        while heap:
            directions = [[0,-1],[0,1],[-1,0],[1,0]]
            dist,x,y = heapq.heappop(heap)
            
            if dist>distances[x][y]:
                continue
            for direction in directions:
                dx = x+direction[0]
                dy = y+direction[1]

                if dx>=0 and dx<n and dy>=0 and dy<m:
                    new_dist = dist + grid[dx][dy]
                    if new_dist<distances[dx][dy]:
                        distances[dx][dy] = new_dist
                        heapq.heappush(heap,(new_dist,dx,dy))
        return distances[n-1][m-1]
                



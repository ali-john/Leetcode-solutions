class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        n = len(grid)
        m = len(grid[0])

        heap = []
        distance = [ [float('inf')]*m for _ in range(n) ]
        if grid[0][0] == 0:
            heapq.heappush(heap, (0,0, 0)) # cost, cost, x, y
        if grid[0][0] == 1:
            heapq.heappush(heap, (1,0, 0))
        
        ans = float('inf')
        while heap:
            dist , x, y = heapq.heappop(heap)
            if dist > distance[x][y]:
                continue
            
            if x == n-1 and y == m-1: # reached the end node
                ans = min(ans, dist)
                break

            for dx, dy in [(0,1),(0,-1),(1,0),(-1,0)]:
                new_x = x + dx
                new_y = y + dy
                if 0 <= new_x < n and 0<= new_y < m:
                    current_dist = dist + grid[new_x][new_y]
                    if distance[new_x][new_y] > current_dist:
                        distance[new_x][new_y] = current_dist
                        heapq.heappush(heap, (current_dist, new_x, new_y))
        
        print(ans)
        return health - ans >= 1

                


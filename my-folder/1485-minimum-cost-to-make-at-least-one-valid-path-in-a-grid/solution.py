class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        distances = [[float('inf')]*cols for _ in range(rows)]
        distances[0][0] = 0
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        heap = [(0,0,0)] # cost,x,y
        while heap:
            cost,x,y = heapq.heappop(heap)
            if distances[x][y]<cost:continue

            for d,(dx,dy) in enumerate(directions):
                new_x = x + dx
                new_y = y + dy
                if new_x>=0 and new_x<rows and new_y>=0 and new_y<cols:
                    new_cost = cost + (d!=(grid[x][y]-1))
                    if new_cost< distances[new_x][new_y]:
                        distances[new_x][new_y] = new_cost
                        heapq.heappush(heap,(new_cost,new_x,new_y))
        return distances[rows-1][cols-1]


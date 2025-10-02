class Solution:
    def minCost(self, m: int, n: int, waitCost: List[List[int]]) -> int:
        # dijkstra solution
        cost = [[float('inf')]*n for _ in range(m)]
        cost[0][0] = 1

        heap = [(1,0,0)]# cost, x, y
        while heap:
            c , x, y = heapq.heappop(heap)
            if c > cost[x][y]: continue
            if x == m-1 and y == n-1: return c - waitCost[0][0]
            # down
            nx, ny = x + 1, y
            if nx < m:
                new_cost = c + waitCost[x][y] + (nx+1)*(ny+1)
                if new_cost < cost[nx][ny]:
                    cost[nx][ny] = new_cost
                    heapq.heappush(heap, (new_cost, nx,ny))
            # right
            nx, ny = x , y + 1
            if ny < n:
                new_cost = c + waitCost[x][y] + (nx+1)*(ny+1)
                if new_cost < cost[nx][ny]:
                    cost[nx][ny] = new_cost
                    heapq.heappush(heap, (new_cost, nx,ny))
        
        return -1





        # memoization solution
        # MAX = 10000000017
        # table = [[MAX]*(m+1) for _ in range(n+1)]
        # table[0][0] = 1

        # def dp(i,j):
        #     if i >=m or j >=n or i<0 or j<0:
        #         return MAX
        #     if i == m-1 and j == n-1:
        #         return m*n

        #     enter = (i+1) * (j+1)
        #     down = dp(i+1,j)
        #     right = dp(i,j+1)

        #     moveCost = enter + min(down, right)
        #     table[i][j] = min(table[i][j], moveCost)
        #     return table[i][j]
        
        # return dp(0,0)

            
                


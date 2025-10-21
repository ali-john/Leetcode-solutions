class Solution:
    def minTimeToReach(self, mv: List[List[int]]) -> int:
        n = len(mv)
        m = len(mv[0])
        distances = [[float('inf')]*m for _ in range(n)]
        heap = [(0,0,0)]# cost, x, y

        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        while heap:
            c, x, y = heapq.heappop(heap)

            if x == n-1 and y == m-1:
                return c
            for dx, dy in directions:
                new_x, new_y = x + dx, y + dy
                if 0 <= new_x < n and 0 <= new_y < m:
                    diff = mv[new_x][new_y] - c
                    if diff <= 0:
                        cost_to_enter = c + 1
                    else:
                        cost_to_enter = c + 1 + diff

                    if cost_to_enter < distances[new_x][new_y]:
                            distances[new_x][new_y] = cost_to_enter
                            heapq.heappush(heap, (cost_to_enter, new_x, new_y))
        return -1


                
                
            
            



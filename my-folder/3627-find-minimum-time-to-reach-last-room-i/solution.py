class Solution:
    def minTimeToReach(self, mt: List[List[int]]) -> int:
        def isvalid(nx, ny):
                return 0 <= nx < len(mt) and 0 <= ny < len(mt[0])
        
        n = len(mt)
        m = len(mt[0])
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        heap = [(0, 0, 0)]
        visited = [[-1] * m for _ in range(n)]
        visited[0][0] = 0
        
        while heap:
            curr, x, y = heapq.heappop(heap)
            
            if x == n - 1 and y == m - 1:
                return curr
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if isvalid(nx, ny):
                    diff = mt[nx][ny] - curr
                    if diff<=0:
                        next_time = curr+1
                    else:
                        next_time = diff+curr+1
                        
                    if visited[nx][ny]<0 or next_time < visited[nx][ny]:  
                        visited[nx][ny] = next_time
                        heapq.heappush(heap, (next_time, nx, ny))
        
        return -1

class Solution:
    def minimumEffortPath(self, h: List[List[int]]) -> int:
        
        m, n = len(h), len(h[0])
        def is_valid(i,j):
            return (i>=0) and (i<m) and (j>=0) and (j<n)
        
        dist = [[float('inf')]*n for _ in range(m)]
        dist[0][0] = 0
        minHeap = [(0,0,0)] # distance, x,y
        directions = [(0,1),(0,-1),(1,0),(-1,0)]

        while minHeap:
            d,r,c = heappop(minHeap)
            if d>dist[r][c]:
                continue
            if r==m-1 and c==n-1:
                return d
            
            for i in range(4):
                newR,newC = r+directions[i][0], c+directions[i][1]
                if is_valid(newR,newC):
                    new_dist = max(d, abs(h[newR][newC] - h[r][c]))
                    if new_dist < dist[newR][newC]:
                        dist[newR][newC] = new_dist
                        heapq.heappush(minHeap,(new_dist,newR,newC))
            

        









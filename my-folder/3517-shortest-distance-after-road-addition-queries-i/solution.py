class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        graph = {i:[] for i in range(n)}
        for i in range(n-1):
            graph[i].append((i+1,1))

        
        def return_shortest():
            # returns shortest path after each query
            distances = [float('inf')]*n
            distances[0]=0
            heap = [(0,0)]

            while heap:
                node,dist = heapq.heappop(heap)
                if node==n-1:
                    return dist
                    
                if dist>distances[node]:
                    continue
                
                for u,d in graph[node]:
                    if dist+d<distances[u]:
                        distances[u] = dist+d
                        heapq.heappush(heap,(u,dist+d))
                
            return distances[n-1]


        answer = [0]*len(queries)
        for i,(start,end) in enumerate(queries):
            graph[start].append((end,1))
            dist = return_shortest()
            answer[i]= dist
        return answer

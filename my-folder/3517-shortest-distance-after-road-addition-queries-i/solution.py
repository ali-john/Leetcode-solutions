class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        output = []
        graph = [[] for _ in range(n)]
        for i in range(n - 1):
            graph[i].append((i + 1, 1))

        def dj():
            distance = [float("inf")]*n
            distance[0] = 0
            min_heap = [(0,0)]
            while min_heap:
                dist, node = heapq.heappop(min_heap)
                if dist>distance[node]:
                    continue
                
                for v,w in graph[node]:
                    new_dist = dist+w
                    if new_dist<distance[v]:
                        distance[v] = new_dist
                        heapq.heappush(min_heap,(new_dist,v))
            return distance[n-1]

        for start,end in queries:
            graph[start].append((end,1))
            d = dj()
            output.append(d)
        return output


            
        


        
        

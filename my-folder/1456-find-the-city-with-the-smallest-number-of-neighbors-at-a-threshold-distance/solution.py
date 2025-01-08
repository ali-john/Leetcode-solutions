class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        graph = defaultdict(list)
        for start,end,w in edges:
            graph[start].append((end,w))
            graph[end].append((start,w))
        
        def dijkstra(start):
            distances = [float('inf')]*n
            distances[start] = 0
            heap = [(0,start)]

            while heap:
                weight ,node = heapq.heappop(heap)
                
                if weight > distances[node]:continue

                for nei,cost in graph[node]:
                    new_weight = cost + weight
                    if distances[nei]> new_weight:
                        distances[nei] = new_weight
                        heapq.heappush(heap,(new_weight,nei))
            return distances

        shortest_dist = {}
        for i in range(n):
            distances = dijkstra(i)
            shortest_dist[i] = sum(1 for d in distances if d>0 and d<=distanceThreshold)
            
        min_neighbors = min(shortest_dist.values())
        possible_ans = [city for city, count in shortest_dist.items() if count == min_neighbors]

        return max(possible_ans)



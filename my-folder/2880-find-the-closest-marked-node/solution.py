class Solution:
    def minimumDistance(self, n: int, edges: List[List[int]], s: int, marked: List[int]) -> int:
        
        graph = defaultdict(list)
        for u,v,w in edges:
            graph[u].append((v,w))
        
        distances = [float('inf')]*n
        distances[s] = 0
        heap = [(0,s)]

        while heap:
            weight,node = heapq.heappop(heap)
            
            for child,w in graph[node]:
                if weight+w < distances[child]:
                    distances[child] = weight+w
                    heapq.heappush(heap,(weight+w,child))
        
        min_distances = []
        for m in marked:
            dist = distances[m]
            min_distances.append(dist)
        return -1 if all(dist==float('inf') for dist in min_distances) else min(min_distances)

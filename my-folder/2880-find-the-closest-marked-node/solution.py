class Solution:
    def minimumDistance(self, n: int, edges: List[List[int]], s: int, marked: List[int]) -> int:
        
        graph = defaultdict(list)
        for u,v,w in edges:
            graph[u].append((v,w))
        
        distances = [float('inf')]*n
        distances[s] = 0

        heap = [(0,s)]
        while heap:
            dist , node = heapq.heappop(heap)

            for nei, w in graph[node]:
                new_w = w + dist
                if new_w < distances[nei]:
                    distances[nei] = new_w
                    heapq.heappush(heap,(new_w,nei))
        
        min_distances = []
        for node in marked:
            min_distances.append(distances[node])
        
        return -1 if all(dist == float('inf') for dist in min_distances) else min(min_distances)
        




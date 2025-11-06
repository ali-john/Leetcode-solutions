class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        graph = defaultdict(list)
        for c1,c2, cost in connections:
            graph[c1].append((cost, c2))
            graph[c2].append((cost, c1))
        
        heap = [(0,n)]
        visited = set()
        total = 0
        while heap:
            cost, city = heapq.heappop(heap)
            if city not in visited:
                visited.add(city)
                total+=cost
                for edge_cost, next_city in graph[city]:
                    heapq.heappush(heap, (edge_cost, next_city))
        return total if len(visited) == n else -1

            
            

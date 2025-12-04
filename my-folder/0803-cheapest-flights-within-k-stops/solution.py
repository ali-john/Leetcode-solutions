class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = {i: [] for i in range(n)}
        for from_, to_, price in flights:
            graph[from_].append([to_, price])
        
        distances = [float('inf')]*n
        distances[src] = 0
        q = [(src,0)] # node, cost
        steps = 0

        while q and steps <= k:
            
            for i in range(len(q)):
                node, cost = q.pop(0)
                for nei, price in graph[node]:
                    if ( price + cost ) > distances[nei]: continue
                    distances[nei] = price + cost
                    q.append((nei, price + cost))
            
            steps+=1
        return distances[dst] if distances[dst]!=float('inf') else -1

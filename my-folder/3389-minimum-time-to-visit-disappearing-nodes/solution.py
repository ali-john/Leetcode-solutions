class Solution:
    def minimumTime(self, n: int, edges: List[List[int]], disappear: List[int]) -> List[int]:
        graph = {i: [] for i in range(n)}
        for u,v,l in edges:
            graph[u].append((v,l))
            graph[v].append((u,l))

        distances = [float('inf')]*n
        distances[0] = 0
        
        heap = [(0,0)] # time, node
        while heap:
            time, node = heapq.heappop(heap)
            if time >= disappear[node] or time>distances[node]: continue
            distances[node] = min(distances[node],time)
            for nei, l in graph[node]:
                next_time = time + l
                if next_time >= disappear[nei]: 
                    continue
                if next_time < distances[nei]:
                    distances[nei] = next_time
                    heapq.heappush(heap, (next_time, nei))
        #print(distances)
        for i in range(n):
            if distances[i] >= disappear[i]:
                distances[i] = -1
        return distances


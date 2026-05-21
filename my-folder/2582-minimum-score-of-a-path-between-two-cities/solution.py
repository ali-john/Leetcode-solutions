class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)
        for start,end,dist in roads:
            graph[start].append((end,dist))
            graph[end].append((start,dist))
        
        #print(graph)
        visited = [False]*(n+1)
        visited[1] = True
        q = [1]
        ans = float('inf')
        while q:
            node = q.pop(0)
            for nei, weight in graph[node]:
                ans = min(ans, weight)
                if not visited[nei]:
                    visited[nei] = True
                    q.append(nei)
        return ans


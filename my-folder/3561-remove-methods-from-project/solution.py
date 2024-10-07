class Solution:
    def remainingMethods(self, n: int, k: int, edges: List[List[int]]) -> List[int]:
        graph = {i: [] for i in range(n)}
        for u,v in edges:
            if u not in graph:
                graph[u] = []
            
            graph[u].append(v)
        
        
        visited = set([k])
        q = []
        q.append(k)
        # iterate over all suspicous methods now
        while q:
            node = q.pop()
            for child in graph.get(node,[]):
                if child not in visited:
                    q.append(child)
                    visited.add(child)
        
        # now we got all suspiciou list

        # now iterate all remainng nodes to see if any non-suspicious can turn suspicious into non:
        ans = []
        for method in range(n):
            if method in visited: continue
            for neighbor in graph[method]:
                if neighbor in visited:
                    return list(range(n))
            ans.append(method)
        return ans













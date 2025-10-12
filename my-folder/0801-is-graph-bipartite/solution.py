class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        
        n = len(graph)
        color = [-1]*n
        q = []
        for node in range(n):
            if color[node] == -1: 
                color[node] = 0
                q.append(node)
                while q:
                    curr = q.pop(0)
                    for nei in graph[curr]:
                        if color[nei] == -1:
                            color[nei] = 1 - color[curr]
                            q.append(nei)
                        elif color[nei] == color[curr]:
                            return False
        return True


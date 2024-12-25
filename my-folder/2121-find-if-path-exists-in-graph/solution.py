class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, dest: int) -> bool:
        
        graph = defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        q = [source]
        visited = set()
        visited.add(source)
        
        while q:
            node = q.pop(0)
            
            if node == dest:
                return True
            
            for nei in graph[node]:
                if nei not in visited:
                    q.append(nei)
                    visited.add(nei)
        return False
            

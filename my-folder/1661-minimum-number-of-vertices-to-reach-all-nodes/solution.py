class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = {i:[] for i in range(n)}
        for u,v in edges:
            graph[u].append(v)
        
        output = []
        in_degrees = set()
        visited = set()
        def dfs(node):
            q = []
            q.append(node)
            while q:
                node = q.pop(0)
                visited.add(node)
                for nei in graph[node]:
                    if nei not in in_degrees:
                        in_degrees.add(nei)
                        q.append(nei)
            
        for node in range(n):
            if node not in visited and node not in in_degrees:
                dfs(node)
        
        all_elements = set([i for i in range(n)])
        return list(all_elements-in_degrees)


        

        

class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, dest: int) -> bool:
        
        graph = defaultdict(set)
    
        for u,v in edges:
            graph[u].add(v)
        
        memo = {}
        def dfs(src,visited):
            if src in visited:
                return False
            if src not in graph:
                return src==dest
            visited.add(src)

            for next_node in graph[src]:
                if not next_node in memo:
                    memo[next_node] = dfs(next_node,visited)
                if not memo[next_node]:
                    return False
            visited.remove(src)
            return True
        
        return dfs(source,set())
                


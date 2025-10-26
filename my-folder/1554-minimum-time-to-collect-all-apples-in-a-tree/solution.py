class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        graph = {i: [] for i in range(n) }
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visited = set()
        def dfs(vertex):
            visited.add(vertex)
            curr = 0
            for nei in graph[vertex]:
                if nei not in visited:
                    curr += dfs(nei)
                    
            if curr > 0 or hasApple[vertex]:
                curr+=2
                return curr    
            else: return 0 
        ans = dfs(0)
        if ans: return ans - 2
        else: return 0





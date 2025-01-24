class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        # 0--unsafe, 1--safe, 2--terminal, -1-->unvisited, -2-->visiting
        states = defaultdict(int)
        for i in range(n): states[i] = -1

        def dfs(node):
            if states[node]!=-1:return 
            states[node] = -2
            if len(graph[node])==0:
                states[node] = 2
            for child in graph[node]:
                dfs(child)
            is_safe = True
            for child in graph[node]:
                if states[child]!=1:
                    states[node] = 0
                    is_safe = False
                    break
            if is_safe:
                states[node] = 1
        for i in range(n):
            dfs(i)
        
        ans = []
        for i in range(n):
            if states[i]==1:
                ans.append(i)
        return sorted(ans)
            

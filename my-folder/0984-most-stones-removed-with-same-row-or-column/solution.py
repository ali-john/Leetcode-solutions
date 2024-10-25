class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        graph = {i:[] for i in range(n)}
        for i in range(n):
            for j in range(i+1,n):
                if stones[i][0]==stones[j][0] or stones[i][1]==stones[j][1]: #any common row/col
                    graph[i].append(j)
                    graph[j].append(i)
        visited = [False]*n
        def dfs(node):
            visited[node] = True
            for neighbour in graph[node]:
                if not visited[neighbour]:
                    dfs(neighbour)
        components = 0
        for i in range(n):
            if not visited[i]:
                dfs(i)
                components+=1
        return n-components




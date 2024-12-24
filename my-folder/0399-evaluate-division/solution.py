class Solution:
    def calcEquation(self, eq: List[List[str]], val: List[float], q: List[List[str]]) -> List[float]:
    
        n = len(eq)
        graph = defaultdict(list)
        for (a,b),cost in zip(eq,val):
            graph[a].append((b,cost))
            graph[b].append((a,1/cost))

        print(graph)
        def dfs(start,end,path_cost,visited):
            
            if start==end:
                return path_cost
            visited.add(start)
            for nei,cost in graph[start]:
                if nei not in visited:
                    value = dfs(nei,end,path_cost*cost,visited)
                    if value is not None:
                        return value
            
        output = [-1]*len(q)

        for i,(start,end) in enumerate(q):
            if start==end and start in graph:
                output[i] = 1
            elif start not in graph or end not in graph:
                output[i] = -1
            else:
                out = dfs(start,end,1,set())
                if out is not None:
                    output[i] = out
        return output
            




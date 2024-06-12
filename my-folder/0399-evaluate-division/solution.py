class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = {}
        output = [-1 for _ in range(len(queries))]
        for i in range(len(equations)):
            x1,x2 = equations[i]
            cost = values[i]
            if x1 not in graph:
                graph[x1] = []
            graph[x1].append((x2,cost))
            if x2 not in graph:
                graph[x2] = []
            graph[x2].append((x1,1/cost))

        def bfs(s,d,graph):
            q = []
            q.append((s,1))
            visited = set()
            total_cost = 1

            while q:
                s,cost = q.pop(0)
                visited.add(s)
                nei = graph.get(s)
                
                for next_n,val in nei:
                    if next_n == d:
                        total_cost = cost* val
                        return total_cost
                    else:
                        qvals = [x for (x,y) in q]
                        if next_n not in visited and next_n not in qvals:
                            new_val = val*cost
                            q.append((next_n,new_val))
            return -1 # not found a path
        index=-1
        keys = graph.keys()
        for q1,q2 in queries:
            index+=1
            if q1 in keys and q2 in keys:
                output[index] = bfs(q1,q2,graph)
        return output

            


                    








        
        
            




        

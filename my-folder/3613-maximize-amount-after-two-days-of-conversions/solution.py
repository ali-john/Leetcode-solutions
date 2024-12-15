class Solution:
    def maxAmount(self, initialCurrency: str, pairs1: List[List[str]], rates1: List[float], pairs2: List[List[str]], rates2: List[float]) -> float:

        graph1 = defaultdict(list)

        for (source,target),rate in zip(pairs1,rates1):
            graph1[source].append((target,rate))
            graph1[target].append((source,1/rate))
        
        graph2 = defaultdict(list)
        for (source, target), rate in zip(pairs2,rates2):
            graph2[source].append((target,rate))
            graph2[target].append((source,1/rate))
        
        def bfs(start,graph):
            max_graph = defaultdict(float)
            q = deque([(curr, start[curr]) for curr in start])
            max_graph.update(start) 
            while q:
                node, val = q.pop()
                for nei, rate in graph[node]:
                    new_rate = rate*val
                    if new_rate > max_graph[nei]:
                        max_graph[nei] = new_rate
                        q.append((nei,new_rate))
            return max_graph
        
        start = {initialCurrency: 1.0}
        day1 = bfs(start, graph1) 
        day2 = bfs(day1, graph2)
        return day2[initialCurrency]


        

        
        
        

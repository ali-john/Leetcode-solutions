class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        output = [0]
        graph = defaultdict(list)

        for v1,v2 in edges:
            graph[v1].append(v2)
            graph[v2].append(v1)
        
        def dfs(curr,parent):
            total = 0

            for nei in graph[curr]:
                if nei != parent:
                    total+= dfs(nei,curr)
                    total = total%k
            total += values[curr]
            total %= k
            if total==0:
                output[0]+=1
            
            return total
        
        dfs(0,-1)
        return output[0]



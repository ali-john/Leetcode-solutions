class Solution:
    def countPairsOfConnectableServers(self, edges: List[List[int]], signalSpeed: int) -> List[int]:
        n = len(edges)+1
        degree = [0]*n
        graph = defaultdict(list[list])

        for node1, node2, w in edges: # build graph
            graph[node1].append([node2,w])
            graph[node2].append([node1,w])
            degree[node1]+=1
            degree[node2]+=1
        
        
        def dfs(node,parent, s):
            
            ans = 0
            if s%signalSpeed==0:
                ans+=1
            
            for next_node,weight in graph[node]:
                if next_node==parent:
                    continue
                ans+= dfs(next_node,node,s+weight)
            
            return ans


        to_process = [1]*n
        for i in range(n):
            if degree[i]==1: # leaf node, do not have connections
                to_process[i]=0
        
        output = [0]*n
        for i in range(n):
            if to_process[i]==1:
                res = []
                for next_node,weight in graph[i]:
                    res.append(dfs(next_node,i, weight))
                total = sum(res)
                ans = 0
                for curr in res:
                    ans+= (total-curr )*curr
                output[i] = ans//2
            else:
                continue
        return output
           

                




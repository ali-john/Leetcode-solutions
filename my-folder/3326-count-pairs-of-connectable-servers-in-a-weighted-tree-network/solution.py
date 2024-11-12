class Solution:
    def countPairsOfConnectableServers(self, edges: List[List[int]], signalSpeed: int) -> List[int]:
        n = len(edges)

        graph = {i:[] for i in range(n+1)}
        
        for node1,node2,w in edges:
            graph[node1].append((node2,w))
            graph[node2].append((node1,w))
        

        def dfs(node,parent,s):
            ans = 0
            if s%signalSpeed==0:
                ans+=1
            
            for child,weight in graph[node]:
                if child!=parent:
                    ans+=dfs(child,node,s+weight)
            return ans

        output = [0]*(n+1)
        for i in range(n+1):
            if len(graph[i])>1:
                res = []
                for next_node,weight in graph[i]:
                    res.append(dfs(next_node,i, weight))
                print(f'i: {i}, res= {res}')
                total = sum(res)
                ans = 0
                for curr in res:
                    ans+= (total-curr )*curr # here calculate how many combination we can form from these connected server. lets say [2,3,4] servers are connected then we are actually
                    # calculating pairs like (2*7)+ (3*6) + (4*5) and we counted duplicates so //2
                output[i] = ans//2
            else:
                continue
        return output
                
        
        
            
            
            

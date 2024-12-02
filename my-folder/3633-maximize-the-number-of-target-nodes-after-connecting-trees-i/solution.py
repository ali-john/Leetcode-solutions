class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:

        def bfs(edges,k):
            n = len(edges)+1
            graph = [[] for _ in range(n)]

            for u,v in edges:
                graph[u].append(v)
                graph[v].append(u)

            ans = [0]*n
            for i in range(n):
                q = [(i,-1,0)] # node, predecessor, dist
                while q:
                    node,pred, dist = q.pop(0)
                    if dist<=k:
                        ans[i]+=1
                    for nei in graph[node]:
                        if nei!=pred:
                            q.append((nei,node,dist+1))
            return ans

        most_value = max(bfs(edges2,k-1))
        return [x+most_value for x in bfs(edges1,k)]
                    
            

from sortedcontainers import SortedSet
class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        graph = { key:[] for key in range(1,c+1)}
        for u,v in connections:
            graph[u].append(v)
            graph[v].append(u)
        components = {key: -1 for key in range(1, c+1)}

        def bfs(node, id_):
            visited = set()
            q = [node]
            while q:
                curr = q.pop(0)
                components[curr] = id_
                visited.add(curr)
                for nei in graph[curr]:
                    if nei not in visited:
                        q.append(nei)
            return 
        # run bfs for each node to update component ids
        id_ = 0
        for component in range(1,c+1):
            if components[component] == -1: # not assigned Id yet
                id_ +=1
                bfs(component, id_)
            
        sorted_list = {i: SortedSet() for i in range(1,id_+1) }
        for component in range(1,c+1):
            sorted_list[components[component]].add(component)
        
        output = []
        for action, node in queries:
            if action == 2:
                sorted_list[components[node]].discard(node)
            else:
                if len(sorted_list[components[node]]) > 0:
                    if node in sorted_list[components[node]]:
                        output.append(node)
                    else:
                        output.append(sorted_list[components[node]][0])
                else:
                    output.append(-1)
        return output















        # TLE ----- O(n^2) solution
        # graph = { key:[] for key in range(1,c+1)}
        # for u,v in connections:
        #     graph[u].append(v)
        #     graph[v].append(u)
        # state = { i: 1 for i in range(1,c+1) }
        
        # def bfs(node):
        #     visited = set()
        #     q = [node]
        #     ans = float('inf')
        #     while q:
        #         curr = q.pop(0)
        #         if state[curr]:
        #             ans = min(ans, curr)
        #         visited.add(curr)
        #         for nei in graph[curr]:
        #             if nei not in visited:
        #                 q.append(nei)
        #     return ans
        # output = []
        # for action,node in queries:
        #     if action == 2:
        #         state[node] = 0
        #         continue
        #     else:
        #         if state[node]:
        #             output.append(node)
        #         else:
        #             ans = bfs(node)
        #             if ans!=float('inf'):
        #                 output.append(ans)
        #             else:
        #                 output.append(-1)
        # return output

                

        
        
        




class Solution:
    def maxStarSum(self, vals: List[int], edges: List[List[int]], k: int) -> int:
        n = len(vals)
        graph = {node: [] for node in range(n)}
        table = {node: [] for node in range(n)}
        
        # build graph:
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        ans = float('-inf')
        for node in range(n):
            neighbors_val = [ vals[nei] for nei in graph[node] ]
            neighbors_val.sort(reverse = True)
            top_k = sum([v for v in neighbors_val[:k] if v > 0])
            ans = max(ans, vals[node] + top_k)
        return ans




        
        
        # def add_topk(node,val):
        #     heap = table[node]
        #     if len(heap) < k:
        #         heapq.heappush(heap,val)
        #     else:
        #         if len(heap) > 0 and val > heap[0]:
        #             heapq.heapreplace(heap,val)
        #     table[node] = heap
            
        # # pre process each node
        # visited = set()
        # for node in range(n):
        #     visited.add(node)
        #     for neighbour in graph[node]:
        #         if neighbour not in visited: 
        #             add_topk(node,vals[neighbour])
        #             add_topk(neighbour, vals[node])
        # # pick most score nodes
        # ans = float('-inf')
        # #print(table)
        # for node in range(n):
        #     # pick positive k neighbours:
        #     heap = table[node]
        #     heap.sort(reverse = True)
        #     #print(f'node: {node}, sorted heap: {heap}')
        #     pos_sum = 0
        #     for i in range(len(heap)):
        #         if heap[i] > 0: pos_sum+=heap[i]
        #     single_node  = vals[node]
        #     curr = max(single_node, single_node + pos_sum)
        #     ans = max(ans, curr)
        # return ans





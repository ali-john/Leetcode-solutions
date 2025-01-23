class Solution:
    def minMaxWeight(self, n: int, edges: List[List[int]], threshold: int) -> int:
        graph = defaultdict(list)
        for u,v, w in edges:
            graph[v].append((u,w)) # reverse edges
        
        # ------------ PRIMS ALGORITHM -------------------------------------
        heap = [(0,0)] # weight,node
        visited = set()
        max_weight = 0
        while heap:
            weight, node = heapq.heappop(heap)
            if node in visited:continue
            max_weight = max(weight,max_weight)
            visited.add(node)
            for child,w_ in graph[node]:
                heapq.heappush(heap,(w_,child))
        return max_weight if len(visited)==n else -1
                



        # ----------------- Binary Search. + DFS -------------------------------------------
        # def is_possible(node,weight_lim,seen):
        #     if node in seen: return
        #     seen.add(node)
        #     for child,w_ in graph[node]:
        #         if w_ > weight_lim: continue
        #         is_possible(child,weight_lim,seen)

            
        # left = 0
        # right = 10000001
        # ans = float('inf')
        # while left<=right:
        #     mid = (left+right)//2
        #     seen = set()
        #     is_possible(0,mid,seen)
        #     if len(seen) ==n:
        #         right = mid - 1
        #         ans = min(ans,mid)
        #     else:
        #         left = mid + 1
        # return ans if ans!=float('inf') else -1

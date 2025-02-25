class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        n = len(edges)
        graph = defaultdict(list)

        for first,second in edges:
            graph[first].append(second)
            graph[second].append(first)
        
        bob_times = defaultdict(int)

        def dfs(src,prev,time):
            if src==0: # if we reached the root
                bob_times[src] = time
                return True
            
            for nei in graph[src]:
                if nei == prev: continue
                if dfs(nei,src,time+1):
                    bob_times[src] = time
                    return True
            return False
        
        dfs(bob,-1,0)

        # alice simulation - BFS
        res = float("-inf")
        q = deque([(0,0,-1,amount[0])]) # node, time, prev, total_profit

        while q:
            node,time, prev, total = q.popleft()

            for nei in graph[node]:
                if nei == prev: continue
                nei_profit = amount[nei]
                nei_time = time + 1
                if nei in bob_times:
                    if nei_time > bob_times[nei]:
                        nei_profit = 0
                    if nei_time == bob_times[nei]: nei_profit = nei_profit // 2
                
                q.append((nei,nei_time,node,total+nei_profit))
                if len(graph[nei]) ==1:
                    res = max(res,total+nei_profit)
        
        return res


            



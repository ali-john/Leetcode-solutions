class Solution:
    def networkDelayTime(self, times: List[List[int]], total: int, k: int) -> int:
        n = len(times)
        graph = defaultdict(list)

        for i, (start,end,time) in enumerate(times):
            graph[start].append((time,end))
        
        heap = [(0,k)]
        visited = set()
        visited.add(k)
        total_times = [float('inf')]*total
        total_times[k-1] = 0
        while heap and len(visited) < total:
            time,node = heapq.heappop(heap)
            for t,nei in graph[node]:
                if nei not in visited:
                    if t+time < total_times[nei-1]:
                        total_times[nei-1] = t+time
                        heapq.heappush(heap,(t+time,nei))
            if node not in visited:
                visited.add(node)
        if len(visited)==total:
            ans = 0
            for time in total_times:
                ans = max(ans,time)
            return ans
        else:
            return -1
                



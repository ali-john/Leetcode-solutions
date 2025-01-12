class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        graph = defaultdict(list)

        for i in range(n):
            graph[i] = []
        
        for i,m in enumerate(manager):
            graph[m].append(i)
        
        max_time = 0
        q = [(headID,informTime[headID])]

        while q:
            node,time = q.pop(0)
            max_time = max(time,max_time)

            for child in graph[node]:
                next_time = time + informTime[child]
                q.append((child,next_time))
        return max_time


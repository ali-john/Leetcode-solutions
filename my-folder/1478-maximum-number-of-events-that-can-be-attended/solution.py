class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events = sorted(events,key = lambda x:(x[0],x[1]))
        ans = 0
        heap = []
        day = 0
        i = 0
        n = len(events)

        while heap or i<n:
            if not heap:
                day = events[i][0]
            
            while i < n and events[i][0] <= day:
                heapq.heappush(heap, events[i][1]) 
                i += 1
            
            while heap and heap[0] < day:
                heapq.heappop(heap)
            
            if heap:
                heapq.heappop(heap)
                ans += 1  

            day += 1
        return ans


        


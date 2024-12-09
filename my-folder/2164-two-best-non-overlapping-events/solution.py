class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events.sort()
        n = len(events)
        
        heap = []
        max_val = 0
        max_sum = 0
        for event in events:
            while heap and heap[0][0]<event[0]:
                max_val = max(max_val,heap[0][1])
                heapq.heappop(heap)
            
            max_sum = max(max_sum,max_val+event[2])
            heapq.heappush(heap,(event[1],event[2]))
        return max_sum
                

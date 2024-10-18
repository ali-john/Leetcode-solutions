class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key= lambda x: x[0])
        heap = []

        for start,end in intervals:
            if heap:
                top = heap[0]
                if start>top:
                    heappop(heap)
            heappush(heap,end)
        return len(heap)



        

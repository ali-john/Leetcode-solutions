class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        n = len(sticks)
        heap = []
        for cost in sticks:
            heapq.heappush(heap,cost)

        total = 0
        while len(heap)>=2:
            val1 = heapq.heappop(heap)
            val2 = heapq.heappop(heap)
            combined = val1+val2
            total+=combined
            heapq.heappush(heap,combined)
        return total

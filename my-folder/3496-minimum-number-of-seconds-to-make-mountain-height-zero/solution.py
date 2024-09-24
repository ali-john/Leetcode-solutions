class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        heap = []
        for i,t in enumerate(workerTimes):
            heap.append((t,1,t))# (total Time,height decremented, base)
        heapq.heapify(heap)

        for _ in range(mountainHeight):
            total_time, height, i = heapq.heappop(heap)
            heapq.heappush(heap, (total_time+(height+1)*i, height+1 ,i))
        return total_time




        

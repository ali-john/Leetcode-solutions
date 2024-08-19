import heapq # its a min heap
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            heapq.heappush(heap,-num)
        output = -heap[0]
        for i in range(k):
            output = -(heapq.heappop(heap))
        return output


                

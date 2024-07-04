import heapq # its a min heap
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pq = []
        heapq.heapify(pq)

        for i in range(len(nums)):
            heapq.heappush(pq,nums[i])
        
        i = len(pq)-k
        output = pq[0]
        while i>=0:
            output = heappop(pq)
            i-=1
        return output
        






        

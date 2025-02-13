class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:

        n = len(nums)
        heap = []

        for num in nums:
            heapq.heappush(heap,num)
        
        op = 0
        while len(heap)>=2:
            n1 = heapq.heappop(heap)
            n2 = heapq.heappop(heap)
            if n1>=k and n2>=k:
                return op
            
            op+=1
            heapq.heappush(heap,min(n1,n2)*2 + max(n1,n2))
        return op
        
        


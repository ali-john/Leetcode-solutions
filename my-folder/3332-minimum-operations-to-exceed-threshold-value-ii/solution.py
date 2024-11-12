class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heap = []

        for num in nums:
            heapq.heappush(heap,num)

        ans =0
        while len(heap)>=2:
            first = heappop(heap)
            second = heappop(heap)
            if first>=k and second>=k:
                return ans
            op = min(first,second)*2 + max(first,second)
            heapq.heappush(heap,op)
            ans+=1


        return ans
        

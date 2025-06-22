class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)
        even_cnt = sum(num%2 == 0 for num in nums)
        odd_cnt = n - even_cnt

        if abs( even_cnt - odd_cnt ) > 1: # impossible case
            return -1
        
        def build_heap():
            even_heap = []
            odd_heap = []

            for i,num in enumerate(nums):
                if num%2 == 0:
                    heapq.heappush(even_heap,i)
                else:
                    heapq.heappush(odd_heap,i)
            return even_heap, odd_heap
        
        def cost(even_at_even: bool) -> int:
            even_h, odd_h = build_heap()
            moves = 0
            for i in range(n):
                if (i % 2 == 0) == even_at_even:
                    moves += abs(i - heapq.heappop(even_h))
                else:
                    moves += abs(i - heapq.heappop(odd_h))
            return moves // 2

        ans = float('inf')
        if even_cnt >= odd_cnt:
            ans = min(ans, cost(True))
        if odd_cnt >= even_cnt:
            ans = min(ans, cost(False))
        
        return ans
        
        






        




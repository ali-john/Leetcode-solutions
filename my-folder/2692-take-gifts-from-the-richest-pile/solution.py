class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        n = len(gifts)
        heap = []

        for num in gifts:
            heapq.heappush(heap,-num)
        
        ans = 0
        for _ in range(k):
            gift = - heapq.heappop(heap)
            taken = math.floor(gift**0.5)
            heapq.heappush(heap,-taken)
        
        for num in heap:
            ans+= (-num)
        return ans



import heapq
class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        table = defaultdict(int)
        for num in arr:
            table[num] += 1
        
        heap = []
        for val in table.values():
            heapq.heappush(heap, val)
        
        while k > 0:
            min_freq = heapq.heappop(heap)
            if k >= min_freq:
                k -= min_freq
            else:
                heapq.heappush(heap, min_freq - k)
                break
        
        return len(heap)

        




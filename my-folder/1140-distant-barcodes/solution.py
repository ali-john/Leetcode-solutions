class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        n = len(barcodes)
        ans = [0]*n
        table = defaultdict(int)
        for i, num in enumerate(barcodes):
            table[num]+=1
        
        heap = []
        for key, val in table.items():
            heapq.heappush(heap, (-val,-key))

        i = 0
        while heap:
            count, val = heapq.heappop(heap)
            count, val = -count, -val
            while count:
                ans[i] = val
                i+=2
                if i>= n:
                    i = 1
                count-=1
        return ans


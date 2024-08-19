from collections import defaultdict
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        table = defaultdict(int)
        for num in nums:
            table[num]+=1
        
        freq = []
        for key,value in table.items():
            heapq.heappush(freq,(-value,key))
        output = []
        for _ in range(k):
            output.append(heapq.heappop(freq)[1])
        return output



        

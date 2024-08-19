from collections import defaultdict
import heapq
class Solution:
    def frequencySort(self, s: str) -> str:
        table = defaultdict(int)
        for char in s:
            table[char]+=1
        
        heap = []
        for key,val in table.items():
            heapq.heappush(heap,(-val,key))
        
        output = ""
        while heap:
            freq ,char = heapq.heappop(heap)
            output+=char*(-freq)
        return output


        

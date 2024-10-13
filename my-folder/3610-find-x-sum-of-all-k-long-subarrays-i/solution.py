from collections import defaultdict, Counter
from typing import List

class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        output = [0] * (n - k + 1)
        table = defaultdict(int)
        for i in range(k):
            table[nums[i]]+=1
        
        def calculate():
            most_common = sorted(table.items(), key = lambda item: (-item[1],-item[0]))
            s = 0
            for idx in range(min(x,len(most_common))):
                s+= most_common[idx][0] * most_common[idx][1]
            return s
        
        output[0] = calculate()
        for i in range(1, n - k + 1):
            incoming = nums[i+k-1]
            outgoing = nums[i-1]
            table[outgoing]-=1
            if table[outgoing]==0:
                del table[outgoing]
            table[incoming]+=1
        
            output[i] = calculate()
        
        return output



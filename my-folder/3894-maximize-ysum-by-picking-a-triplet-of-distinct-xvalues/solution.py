class Solution:
    def maxSumDistinctTriplet(self, x: List[int], y: List[int]) -> int:


        n = len(x)
        table = defaultdict(int)

        for i, num in enumerate(x):
            if num in table:
                table[num] = max(table[num], y[i])
            else:
                table[num] = y[i]

        if len(table.keys()) < 3:
            return -1
        
        vals = sorted(table.values(), reverse = True)
        ans = 0
        for i in range(3):
            ans+=vals[i]

        return ans
        
        
        

class Solution:
    def countWays(self, ranges: List[List[int]]) -> int:
        MOD = 1000000007
        n = len(ranges)
        groups = 0

        ranges = sorted(ranges, key = lambda x: x[0])
        i = 0
        while i < n:
            start, end = ranges[i]
            j = i+1
            while j<n and ranges[j][0] <= end:
                end = max(end, ranges[j][1])
                i = j
                j+=1
                
            groups = (groups + 1)%MOD
            i+=1
       
        return (2**groups)%MOD



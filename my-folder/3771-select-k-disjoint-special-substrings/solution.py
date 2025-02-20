class Solution:
    def maxSubstringLength(self, s: str, k: int) -> bool:
        n = len(s)
        first, end = {}, {}

        # map start and end of each character
        for i, c in enumerate(s):
            if c not in first:
                first[c] = i
            end[c] = i
        
        # print(f'first: {first}')
        # print(f'second: {end}')

        # expand the intervals, see if current char is driving the interval or any char from start
        # or end is driving the interval
        for c in first:
            for i in range(first[c],end[c]):
                new_char = s[i]
                first[c] = min(first[c],first[new_char])
                end[c] = max(end[c],end[new_char])
        
        # print(f'first: {first}')
        # print(f'second: {end}')
        dp = [0 for _ in range(n+1)]
        for i,c in enumerate(s):
            dp[i+1] = dp[i]
            if end[c]==i and (first[c]!=0 or i!=n-1):
                dp[i+1] = max(dp[i+1], 1+dp[first[c]])
        
        return dp[-1]>=k
        

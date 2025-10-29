class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        ans = 0
        for i in range(min(n,limit)+1):
            if n - i > 2*limit: continue
            ans+= min(n-i, limit) - max(0,n-i-limit) + 1
        return ans

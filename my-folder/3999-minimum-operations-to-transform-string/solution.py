class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)
        ans = float('-inf')

        for i in range(n):
            ops = ( 26 - (ord(s[i]) - ord("a")) ) % 26
            ans = max(ans,ops )
        return ans


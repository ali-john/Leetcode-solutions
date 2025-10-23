class Solution:
    def minInsertions(self, s: str) -> int:
        @cache
        def dp(l,r):
            if l >=r: return 0

            if s[l] == s[r]: return dp(l+1, r- 1)
            else:
                return 1 + min(dp(l, r -1), dp(l+1, r))
        return dp(0,len(s) - 1)




class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        s2 = s[::-1]
        
        @cache
        def solve(i,j):
            if i >= n or j >=n: return 0
            ans = 0
            if s[i] == s2[j]:
                ans = 1 + solve(i+1, j+1)
            else:
                cond1 = solve(i+1,j)
                cond2 = solve(i,j+1)
                ans = max(cond1, cond2)
            return ans
        return solve(0,0)

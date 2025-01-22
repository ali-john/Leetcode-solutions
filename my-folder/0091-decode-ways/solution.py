class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        if s[0]=='0':return 0
        
        @cache
        def dp(i):
            if i==n:return 1
            if s[i]=='0':return 0
            if i == n-1:
                return 1
            ans = dp(i+1)
            if int(s[i:i+2])<=26:
                ans+=dp(i+2)
            return ans
        return dp(0)


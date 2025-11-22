class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        n = len(s)

        @cache
        def dp(i, j):
            if i >= j: return 0

            if s[i] == s[j]:
                return dp(i+1, j - 1)
            else:
                cond1 =  dp(i+1, j)
                cond2 =  dp(i, j-1)
                return 1 + min(cond1, cond2)
        insertions = dp(0, len(s) - 1)
        return insertions <= k
            

        
        
        
        
        
        
        # s_dup = s[::-1]

        # @cache
        # def dp(i,j):
        #     if i >=n or j>=n: return 0
        #     ans = 0
        #     if s[i] == s_dup[j]:
        #         ans = 1 + dp(i+1, j+1)
        #     else:
        #         cond1 = dp(i+1, j)
        #         cond2 = dp(i, j+1)
        #         ans = max(cond1, cond2)
        #     return ans
        # max_palindrome = dp(0,0)
        # #print(max_palindrome)
        # return ( n - max_palindrome ) <= k



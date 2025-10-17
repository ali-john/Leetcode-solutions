class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        ans = ""
        ans_len = float('-inf')

        # treat every index as stating point of palindrome
        for i in range(n):
            # if odd length
            l,r = i, i
            while l >= 0 and r < n and s[l] == s[r]:
                if (r-l + 1) > ans_len:
                    ans_len = (r-l + 1)
                    ans = s[l:r+1]
                l-=1
                r+=1
            
            # if even
            l ,r = i,  i + 1
            while l >= 0 and r < n and s[l] == s[r]:
                if (r-l + 1) > ans_len:
                    ans_len = (r-l + 1)
                    ans = s[l:r+1]
                l-=1
                r+=1
        return ans

            










        # n = len(s)
        # if n == 1: return s
        # ans = float('-inf')  
        # output = s[0]      
        # for i in range(n):
        #     for j in range(i+1,n):
        #         substr = s[i:j+1]
        #         if substr == substr[::-1]:
        #             if len(substr) > ans:
        #                 ans = len(substr)
        #                 output = substr
        # return output





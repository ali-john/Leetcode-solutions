class Solution:
    def longestPalindrome(self, s: str) -> str:
        output = ""
        output_len = 0
        n = len(s)
        for i in range(n):
            # if n is odd:
            l,r = i, i 
            while l>=0 and r<n and s[l]==s[r]:
                if (r-l+1)>output_len:
                    output = s[l:r+1]
                    output_len = (r-l+1)
                l-=1
                r+=1
            
            # odd case:
            l,r = i, i+1
            while l>=0 and r<n and s[l]==s[r]:
                if (r-l+1)>output_len:
                    output = s[l:r+1]
                    output_len = (r-l+1)
                l-=1
                r+=1
        return output


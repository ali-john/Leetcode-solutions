class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        ans = 0

        for i in range(len(s)):
            for j in range(len(t)):
                count = 0
                k = 0
                while k+i< len(s) and k+j<len(t):
                    if s[i+k]!=t[j+k]:
                        count+=1
                    if count==1:
                        ans+=1
                    if count>1:
                        break
                    k+=1
        return ans



class Solution:
    def numOfSubsequences(self, s: str) -> int:
        n = len(s)
        prefix = [0]*(n+1)
        suffix = [0]*(n+1)

        for i in range(n):
            if s[i] == 'L':
                prefix[i+1] = 1
            prefix[i+1] += prefix[i]
        
        for i in range(n-1, -1, -1):
            if s[i] == 'T':
                suffix[i] = 1
            suffix[i]+=suffix[i+1]
        
        resWithC = 0
        bestWithC = 0
        resWithL = 0
        resWithT = 0
        for i in range(n):
            if s[i] == 'C':
                resWithC+= prefix[i] * suffix[i+1]
                resWithL += (prefix[i]+1) * suffix[i+1]
                resWithT+= prefix[i] * (suffix[i+1] + 1)
            else:
                bestWithC = max(bestWithC, prefix[i]*suffix[i])
        resWithC += bestWithC
        return max(resWithC, resWithL, resWithT)

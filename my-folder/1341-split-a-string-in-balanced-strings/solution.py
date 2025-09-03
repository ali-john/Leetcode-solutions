class Solution:
    def balancedStringSplit(self, s: str) -> int:
        n = len(s)
        ans = 0
        balance = 0

        for i in range(n):
            if s[i] == 'R':
                balance+=1
            else:
                balance-=1
            
            if balance == 0:
                ans+=1
        return ans

class Solution:
    def minimumSteps(self, s: str) -> int:

        swaps = 0
        n = len(s)
        ones = 0
        for i in range(n):
            if s[i]=='1':
                ones+=1

            else:
                swaps+=ones
        return swaps
            

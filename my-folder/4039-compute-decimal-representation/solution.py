class Solution:
    def decimalRepresentation(self, n: int) -> List[int]:
        ans = []

        divisor = 10
        while n:
            dividend = n%divisor
            if dividend>0:
                ans.append(dividend)
            divisor*=10
            n-=dividend
        ans.sort(reverse = True)
        return ans

        
        

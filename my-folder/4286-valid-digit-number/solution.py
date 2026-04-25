class Solution:
    def validDigit(self, n: int, x: int) -> bool:
        digits = []
        while n:
            digits.append(n%10)
            n//=10
        
        return x in digits and x!=digits[-1]

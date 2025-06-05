class Solution:
    def isHappy(self, n: int) -> bool:
        s = set()

        while True:
            digits = [int(digit) for digit in str(n)]
            n = sum([digit**2 for digit in digits])
            if n == 1:
                return True
            if n in s:
                return False
            s.add(n)
        
        return True
        

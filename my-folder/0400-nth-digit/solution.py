class Solution:
    def findNthDigit(self, n: int) -> int:
        if n<=9:
            return n
        
        base = 9
        digit = 1

        while n > base*digit:
            n-= base*digit
            base *= 10
            digit+=1
        num = 10**(digit-1) + (n-1)//digit
        idx = (n-1)%(digit)
        return int(str(num)[idx])

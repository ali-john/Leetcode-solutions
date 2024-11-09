class Solution:
    def smallestNumber(self, n: int, t: int) -> int:

        while True:
            digits = [int (digit) for digit in str(n)]
            product = math.prod(digits)
            if product%t==0:
                return n
            else:
                n+=1
        
        

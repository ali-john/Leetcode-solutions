class Solution:
    def sumAndMultiply(self, n: int) -> int:
        str_n = str(n)
        if all(x == '0' for x in str_n):
            return 0
        non_zero = []
        for digit in str_n:
            if digit!= '0':
                non_zero.append(digit)
        x = int( "".join(non_zero) )
        s = sum([int(digit) for digit in non_zero ])
        # print(x)
        # print(s)
        return x*s
        

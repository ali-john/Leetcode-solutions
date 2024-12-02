class Solution:
    def smallestNumber(self, n: int) -> int:
        n_bin = bin(n)[2:]
        output = '1'*len(n_bin)
        return int(output,2)
        
        

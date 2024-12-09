class Solution:
    def maximumXorProduct(self, a: int, b: int, n: int) -> int:
        a_copy = a
        b_copy = b
        MOD = 10**9 + 7
        res = 0

        for i in range(n-1,-1,-1):
            shift = 1<<i
            a_bit = a & shift
            b_bit = b & shift

            if not a_bit and not b_bit:
                res |= shift
            
            if a_bit and b_bit:
                continue
            
            if a>b:
                if a_bit:
                    a ^= shift
                    b ^= shift
                    res |= shift
            elif b>a:
                if b_bit:
                    a ^= shift
                    b ^= shift
                    res |= shift
        return (a_copy ^ res) * (b_copy ^ res) % MOD


class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7
        def fast_pow(b, exp):
            if exp == 0:
                return 1
            else:
                res = fast_pow(b, exp//2)
                return res*res*(b if exp%2 else 1) % MOD
        
        return fast_pow(5, (n+1)//2) * fast_pow(4, n//2) % MOD

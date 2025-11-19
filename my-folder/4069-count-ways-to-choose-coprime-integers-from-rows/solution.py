class Solution:
    def countCoprime(self, mat: List[List[int]]) -> int:
        MOD = 10**9 + 7
        n = len(mat)
        m = len(mat[0])

        @cache
        def dp(row, curr_gcd):
            if row == n:
                return 1 if curr_gcd == 1 else 0
            
            total = 0
            for c in range(m):
                new_gcd = gcd(curr_gcd, mat[row][c])
                total = ( total + dp(row+1, new_gcd) ) % MOD
            return total
        
        ans = 0
        for c in range(m):
            ans = ( ans + dp(1, mat[0][c])) % MOD
        return ans

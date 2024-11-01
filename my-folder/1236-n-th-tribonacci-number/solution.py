class Solution:
    def tribonacci(self, n: int) -> int:
        table = {0:0,
                 1:1,
                 2:1
        }

        def solve(n):
            if n<0:
                return 0
            if n in table:
                return table[n]

            ans = solve(n-1)+solve(n-2)+solve(n-3)
            table[n] = ans
            return ans
        return solve(n)


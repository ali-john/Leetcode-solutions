class Solution:
    def minSensors(self, n: int, m: int, k: int) -> int:
        coverage = 2*k + 1
        rows = math.ceil(n / coverage)
        cols = math.ceil(m / coverage)

        ans = rows*cols
        return ans

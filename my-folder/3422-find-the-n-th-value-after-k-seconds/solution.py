class Solution:
    def valueAfterKSeconds(self, n: int, k: int) -> int:
        MOD = 1000000007
        arr = [1]*n

        while k:
            for i in range(1, n):
                arr[i] = (arr[i] + arr[i-1])%MOD
            k-=1
        return arr[n-1]%MOD

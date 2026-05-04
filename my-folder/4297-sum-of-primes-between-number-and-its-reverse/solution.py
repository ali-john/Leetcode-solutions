class Solution:
    def sumOfPrimesInRange(self, n: int) -> int:
        def is_prime(num):
            return num > 1 and all(num % i != 0 for i in range(2, int(num**0.5) + 1))
        rev_n = int(str(n)[::-1])
        min_ = min(n, rev_n)
        max_ = max(n, rev_n)
        ans = 0
        for num in range(min_, max_+1):
            if is_prime(num):
                #print(f'Prime: {num}')
                ans+=num
        return ans

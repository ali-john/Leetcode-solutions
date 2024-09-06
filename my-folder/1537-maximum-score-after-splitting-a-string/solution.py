class Solution:
    def maxScore(self, s: str) -> int:
        ll = [int(char) for char in s ]
        n = len(ll)
        prefix = [0]*n
        prev = 0
        for i in range(n):
            prev+=ll[i]
            prefix[i]=prev
        
        max_count = 0

        for i in range(n-1):
            pre = prefix[i]
            zeros = i - pre +1
            ones = prefix[-1] - prefix[i]
            max_count = max(max_count, (zeros+ones))
        return max_count

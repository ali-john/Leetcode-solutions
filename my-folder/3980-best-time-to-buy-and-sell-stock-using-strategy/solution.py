class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        n = len(prices)
        original = sum(prices[i] * strategy[i] for i in range(n))
        
        windowSum = 0
        for i in range(k//2, k, 1):
            windowSum+=prices[i]
        
        for i in range(k,n,1):
            windowSum+=prices[i]*strategy[i]
        ans = max(original, windowSum)

        for end in range(k,n,1):
            start = end - k + 1
            windowSum += prices[start-1]*strategy[start-1]
            midIdx = start+ k//2  - 1
            windowSum-=prices[midIdx]

            windowSum-=prices[end]*strategy[end]
            windowSum+=prices[end]

            ans = max(ans, windowSum)
        return ans


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        max_ans = 0
        min_price = float('inf')

        for i in range(n):
            if prices[i]<min_price:
                min_price = prices[i]
            
            elif prices[i] - min_price > max_ans:
                max_ans = prices[i] - min_price
        return max_ans

        
            
            



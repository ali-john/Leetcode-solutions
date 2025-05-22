class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        n = len(prices)
        max_ans = -1
        min_val = float('inf')

        for i in range(n):
            if prices[i] < min_val:
                min_val = prices[i]
            
            if prices[i] - min_val > max_ans:
                max_ans = max(max_ans, prices[i] - min_val)
        return max_ans


        
            
            



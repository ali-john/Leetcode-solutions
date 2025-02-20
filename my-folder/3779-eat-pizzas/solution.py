class Solution:
    def maxWeight(self, pizzas: List[int]) -> int:
        pizzas.sort()
        days = len(pizzas)//4
        even_days = days//2
        odd_days = days-even_days
        ans = 0
        for _ in range(odd_days):
            ans += pizzas.pop()
        for  _ in range(even_days):
            pizzas.pop()
            ans += pizzas.pop()
        return ans

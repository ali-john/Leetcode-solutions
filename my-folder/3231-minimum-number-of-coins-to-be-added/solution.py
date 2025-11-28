class Solution:
    def minimumAddedCoins(self, coins: List[int], target: int) -> int:
        n = len(coins)
        coins.sort()
        res = 0
        curr = 0
        i = 0
        while curr < target:
            if i < n and coins[i] <= curr + 1:
                curr+=coins[i]
                i+=1
            else:
                res+=1
                curr+= curr+1
        return res


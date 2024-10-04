class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        n = len(cards)
        table = defaultdict(int)

        ans = float("inf")
        for i in range(n):
            if cards[i] in table:
                ans = min(ans,(i-table[cards[i]]+1))
            
            table[cards[i]] = i
        return ans if ans!=float("inf") else -1


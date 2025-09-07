class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        n  = len(happiness)
        ans = 0
        happiness.sort(reverse=True)
        for i in range(k):
            ans += max(happiness[i] - i, 0)
        return ans

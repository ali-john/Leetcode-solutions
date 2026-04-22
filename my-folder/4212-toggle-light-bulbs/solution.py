class Solution:
    def toggleLightBulbs(self, bulbs: list[int]) -> list[int]:
        c = Counter(bulbs)
        ans = []
        for b,count in c.items():
            if count%2 != 0:
                ans.append(b)
        ans = sorted(ans)
        return ans

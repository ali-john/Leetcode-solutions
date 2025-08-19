class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        n = len(target)
        count_table = Counter(target)
        count_s = Counter(s)

        ans = float('inf')
        for char, val in count_table.items():
            if count_s[char] >=val:
                pairs = count_s[char] // val
                ans = min(ans, pairs)
            else:
                ans = 0
                return ans
            
        return ans

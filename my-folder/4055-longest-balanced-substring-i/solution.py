class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        ans = 1
        for i in range(n):
            table = defaultdict(int)
            table[s[i]] = 1
            for j in range(i+1,n):
                table[s[j]] = table[s[j]] + 1
                # check if balanced
                keys = set(list(table.keys()))
                is_balanced = True
                for key in keys:
                    if table[key] != table[s[i]]:
                        is_balanced = False
                        break
                if is_balanced:
                    ans = max(ans, j-i + 1)
        return ans



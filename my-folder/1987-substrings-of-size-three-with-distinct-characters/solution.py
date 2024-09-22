class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        n = len(s)
        total = 0
        for i in range(n-2):
            window = s[i:i+3]
            if len(set(window))==3:
                total+=1

        return total


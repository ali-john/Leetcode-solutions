class Solution:
    def firstMatchingIndex(self, s: str) -> int:
        n = len(s)
        for i in range(n//2 + 1):
            end = n - i - 1
            if end>= i:
                if s[i] == s[end]:
                    return i
            else:
                break
        return -1

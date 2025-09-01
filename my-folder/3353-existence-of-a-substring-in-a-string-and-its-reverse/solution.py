class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        n = len(s)
        if n== 1:
            return False
        reverse_s = "".join(reversed(s))
        substrings = []
        for i in range(n-1):
            substrings.append(s[i:i+2])
        
        for substring in substrings:
            if substring in reverse_s:
                return True
        return False


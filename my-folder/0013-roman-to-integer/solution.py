class Solution:
    def romanToInt(self, s: str) -> int:
        table = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        n = len(s)
        i = 0
        total = 0

        while i<n:
            if i+1 < n and table[s[i+1]] > table[s[i]]:
                total+= table[s[i+1]] - table[s[i]]
                i+=2
            else:
                total+= table[s[i]]
                i+=1
        return total




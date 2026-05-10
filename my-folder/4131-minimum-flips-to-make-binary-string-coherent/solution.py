class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        ones = s.count("1")
        zeros = s.count("0")

        if ones == 0 or zeros == 0:
            return 0
        if s[0] == '1' and s[-1] == '1':
            return min(zeros, ones - 2)

        return min(ones - 1, zeros)

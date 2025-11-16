class Solution:
    def minLengthAfterRemovals(self, s: str) -> int:
        table = Counter(s)
        return abs( table['b'] - table['a'] )

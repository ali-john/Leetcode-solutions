class Solution:
    def maxDistinct(self, s: str) -> int:
        return len( Counter(s).keys() )

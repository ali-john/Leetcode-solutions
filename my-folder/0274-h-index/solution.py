class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        citations = sorted(citations)
        h_index = 0

        for i in range(citations[-1]+1):
            index = bisect_left(citations,i)
            if n - index >= i:
                h_index = max(h_index,i)
        return h_index


class Solution:
    def maximumSumOfHeights(self, heights: List[int]) -> int:
        n = len(heights)
        max_ans = float('-inf')

        for i in range(n):
            heights_copy = heights[:]
            for j in range(i-1, -1, -1):
                heights_copy[j] = min(heights_copy[j], heights_copy[j+1])
            for j in range(i+1, n, 1):
                heights_copy[j] = min( heights_copy[j], heights_copy[j - 1] )
            
            max_ans = max(max_ans, sum(heights_copy))
        return max_ans




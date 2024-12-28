class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        n = len(values)

        max_left_scores = [0]*n
        max_left_scores[0] = values[0]

        max_score = 0

        for i in range(1,n):
            left = max_left_scores[i-1]
            curr_val = values[i] - i
            max_score = max(max_score,left+curr_val)

            max_left_scores[i] = max(max_left_scores[i-1],values[i]+i)
        return max_score

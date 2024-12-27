class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        n = len(values)

        left_scores = [0]*n
        left_scores[0] = values[0]

        max_score = 0

        for i in range(1,n):
            curr_left_score = left_scores[i-1]

            curr_score = (values[i] - i) + curr_left_score
            max_score = max(max_score,curr_score)
            curr_left_score = max(curr_left_score,values[i]+i)
            left_scores[i] = curr_left_score
        return max_score

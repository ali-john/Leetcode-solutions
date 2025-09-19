class Solution:
    def earliestTime(self, tasks: List[List[int]]) -> int:
        n = len(tasks)

        ans = float("inf")
        for i in range(n):
            start, end = tasks[i]
            time = start + end
            ans = min(ans, time)
        return ans

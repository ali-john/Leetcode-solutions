class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        n = len(startTime)
        gaps = []
        gaps.append(startTime[0]-0)
        for i in range(1,n):
            gaps.append(startTime[i] - endTime[i-1])
        gaps.append(eventTime - endTime[-1])

        m = len(gaps)
        window = k+1
        curr = sum(gaps[:window])
        max_ans = curr
        for i in range(window,m):
            curr+=gaps[i] - gaps[i-window]
            max_ans = max(max_ans,curr)
        return max_ans


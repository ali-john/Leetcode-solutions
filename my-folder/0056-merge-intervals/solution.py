class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        intervals.sort(key = lambda x : x[0])

        output = []
        i = 0
        while i < n:
            left = intervals[i][0]
            right = intervals[i][1]
            start = i + 1

            while start < n and right >= intervals[start][0]:
                right = max(right, intervals[start][1])
                start+=1
            
            if start == i+1: # no overlap found
                output.append(intervals[i])
                i+=1
            else:
                output.append([left,right])
                i = start
        return output

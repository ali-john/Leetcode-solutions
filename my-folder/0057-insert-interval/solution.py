class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        updated = []

        if n == 0:
            return [newInterval]
        inserted = False
        for i in range(n):
            if intervals[i][0] >= newInterval[0] and not inserted:
                updated.append(newInterval)
                inserted = True
            updated.append(intervals[i])
        if not inserted: # it means insert at end ?
            updated.append(newInterval)
        
        # merge intervals
        n = len(updated)

        output = []
        i = 0

        while i < n:
            left = updated[i][0]
            right = updated[i][1]
            start = i + 1

            while start < n and right >= updated[start][0]:
                right = max(right, updated[start][1])
                start+=1
            
            if start == i+1:
                output.append(updated[i])
                i+=1
            else:
                output.append([left,right])
                i = start
        return output


        

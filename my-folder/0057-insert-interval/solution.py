class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        sorted_list = sorted(intervals,key=lambda x:x[0])
        output = []
        i = 0
        while(i<len(sorted_list)):
            start = i
            max_end = sorted_list[i][1]
            while i+1<len(sorted_list) and sorted_list[i+1][0]<=max_end:
                max_end = max(max_end,sorted_list[i+1][1])
                i+=1
            l = []
            l.append(sorted_list[start][0])
            l.append(max_end)
            output.append(l)
            i+=1
        return output

        

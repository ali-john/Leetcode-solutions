class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        n = len(points)
        points.sort(key = lambda x: x[0])

        output = []

        i = 0
        while i < n:
            left = points[i][0]
            right = points[i][1]
            start = i + 1

            while start < n and right >= points[start][0]:
                right = min(right, points[start][1])
                start+=1
            
            if start == i+1:
                output.append(points[i])
                i+=1
            else:
                output.append([left,right])
                i = start
        
        #print(output)
        return len(output)

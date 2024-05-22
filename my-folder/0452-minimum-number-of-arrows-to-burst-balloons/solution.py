class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        sorted_points = sorted(points,key=lambda x:x[1])
        print(sorted_points)
        arrows = 0
        i = 0

        while(i<len(sorted_points)):
            start = i
            max_end = sorted_points[i][1]
            arrows+=1
            while i+1<len(sorted_points) and sorted_points[i+1][0]<=max_end:
                i+=1
            i+=1
        return arrows
            


        

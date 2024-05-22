class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        slopes = {}
        max_slope=2
        if len(points)==1:
            return 1
        elif len(points)==2:
            return 2
        else:
            for i in range(len(points)):
                x1,y1 = points[i]
                for j in range(len(points)):
                    if i!=j:
                        x2,y2 = points[j]
                        s = math.atan2(y2-y1,x2-x1)
                        slopes[s]=slopes.get(s,0)+1
                max_slope = max(max_slope,(max(slopes.values())+1))
                slopes.clear()
            return max_slope

        

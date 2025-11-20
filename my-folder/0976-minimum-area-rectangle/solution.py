class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        n = len(points)
        s = set()
        for point in points:
            x,y = point
            s.add((x,y))
        
        ans = float('inf')
        for i in range(n):
            for j in range(i+1, n):
                x1, y1 = points[i]
                x2, y2 = points[j]
                if x1!=x2 and y1!=y2:
                    if (x2,y1) in s and (x1, y2) in s:
                        area = abs(x2 - x1) * abs(y2 - y1)
                        #print(f'area: {area}')
                        ans = min(ans, area)
        return ans if ans!=float('inf') else 0

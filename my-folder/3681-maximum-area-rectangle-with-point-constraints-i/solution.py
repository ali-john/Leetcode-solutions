class Solution:
    def maxRectangleArea(self, points: List[List[int]]) -> int:
        points_set = set(map(tuple,points))
        n = len(points)
        max_area = -1


        def has_point_inside(x_min,x_max,y_min,y_max,corners):
            for point in points:
                if tuple(point) in corners:
                    continue
                
                else:
                    x,y = point[0],point[1]
                    if x_min < x < x_max and y_min < y < y_max:
                        return True
                    if (x == x_min or x==x_max) and (y_min <= y <= y_max):
                        return True
                    if (x_min <= x <= x_max) and (y == y_min or y == y_max):
                        return True
            return False


        for i in range(n):
            for j in range(i+1,n):
                x1,y1 = points[i][0], points[i][1]
                x2,y2 = points[j][0],points[j][1]

                if x1!=x2 and y1!=y2:
                    corners = {(x1,y1),(x2,y2),(x2,y1),(x1,y2)}
                    p1 = (x2,y1)
                    p2 = (x1,y2)

                    if p1 in points_set and p2 in points_set:
                        if not has_point_inside(min(x1,x2),max(x1,x2),min(y1,y2),max(y1,y2),corners):
                            area = abs(x1-x2)*abs(y1-y2)
                            max_area = max(max_area,area)
        if max_area!=-1: 
            return max_area
        else:
            return -1





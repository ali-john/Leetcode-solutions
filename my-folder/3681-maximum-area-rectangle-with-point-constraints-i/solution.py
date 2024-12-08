class Solution:
    def maxRectangleArea(self, points: List[List[int]]) -> int:
        point_set = set(tuple(p) for p in points)
        max_area = -1

        def has_points_inside(x_min, x_max, y_min, y_max, corners):
            for px, py in points:
                if (px, py) in corners:
                    continue
                if x_min < px < x_max and y_min < py < y_max:
                    return True
                if (px == x_min or px == x_max) and y_min <= py <= y_max:
                    return True  
                if (py == y_min or py == y_max) and x_min <= px <= x_max:
                    return True  
            return False
    
        n = len(points)
        for i in range(n):
            for j in range(i + 1, n):
                x1, y1 = points[i]
                x2, y2 = points[j]
    
                if x1 != x2 and y1 != y2:
                    corners = {(x1, y1), (x1, y2), (x2, y1), (x2, y2)}
                    if (x1, y2) in point_set and (x2, y1) in point_set:
                        if not has_points_inside(
                            min(x1, x2), max(x1, x2), min(y1, y2), max(y1, y2), corners
                        ):
                            area = abs(x2 - x1) * abs(y2 - y1)
                            max_area = max(max_area, area)
    
        return max_area if max_area != -1 else -1

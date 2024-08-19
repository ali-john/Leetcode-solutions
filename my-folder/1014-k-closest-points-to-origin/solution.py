import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def calculate(point):
            x,y = point[0],point[1]
            dist = ((x**2) + (y**2))
            return dist
        min_distances = []
        for point in points:
            dist = calculate(point)
            heapq.heappush(min_distances,(dist,point))
        output = []
        for _ in range(k):
             output.append(heapq.heappop(min_distances)[1])
        return output

        

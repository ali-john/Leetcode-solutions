class Solution:
    def bestCoordinate(self, towers: List[List[int]], radius: int) -> List[int]:
        def getQuality(x,y):
            ans = 0
            for cx, cy, q in towers:
                d = ((cx - x)**2 + (cy -y)**2)**0.5
                if d <= radius:
                    ans+=floor(q/(1+d))
            return ans

        strength = float('-inf')
        for x in range(51):
            for y in range(51):
                q_curr = getQuality(x,y)
                if q_curr > strength:
                    strength = q_curr
                    coordinates = [x,y]
        return coordinates

                




        

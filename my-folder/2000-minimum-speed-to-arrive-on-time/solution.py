class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        n = len(dist)
        if n > ceil(hour):
            return -1
        
        def is_possible(mid):
            total_hour = 0
            for i in range(n):
                if i == n - 1:
                    total_hour+=(dist[i]/mid)
                else:
                    total_hour += ceil(dist[i] / mid)
            return total_hour <= hour

        
        left = 1
        right = 10**7 + 1
        ans = float('inf')
        while left<=right:
            mid = (left+right) // 2
            if is_possible(mid):
                right = mid - 1
                ans = min(ans, mid)
            else:
                left = mid + 1
        return ans
            


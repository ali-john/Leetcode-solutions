class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        n = len(time)
        time = sorted(time)

        def is_possible(limit):
            #print(f'Limit Given: {limit}')
            trips = 0
            for num in time:
                trips+= int(limit//num)
                #print(f'Total Trips: {trips}')
                if trips >= totalTrips:
                    return True
            return False

        left = min(time)
        right = min(time)*totalTrips
        ans = float('inf')
        while left <= right:
            mid = (left+right) // 2
            if is_possible(mid):
                ans = min(ans, mid)
                right = mid - 1
            else:
                left = mid + 1
        
        return ans


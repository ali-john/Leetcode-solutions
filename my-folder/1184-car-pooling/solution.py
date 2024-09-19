import heapq

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips = sorted(trips, key=lambda x: x[1])
        heap = []
        total_c = 0
        
        for trip in trips:
            c, start, end = trip
            while heap and heap[0][0] <= start:
                total_c -= heapq.heappop(heap)[1]
            
            total_c += c
            
            if total_c > capacity:
                return False
            
            heapq.heappush(heap, (end, c))
        
        return True


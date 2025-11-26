class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        n = len(costs)
        start_heap, end_heap = [], []
        left, right = 0, n-1
        for _ in range(candidates):
            if left > right:
                break
            heapq.heappush(start_heap, (costs[left], left))
            left+=1
        
        for _ in range(candidates):
            if left > right:
                break
            heapq.heappush(end_heap, (costs[right], right))
            right-=1
        
        # print(f'processed: {processed}')
        # print(f'start_heap: {start_heap}')
        # print(f'end_heap: {end_heap}')

        #print(f'start_heap[0][0]: {start_heap[0][0]} ')
        cost = 0
        while k:
            if ( len(start_heap)>0 and len(end_heap) > 0) and (start_heap[0][0] <= end_heap[0][0]):
                #print(f'taking from start_heap')
                val, _ = heapq.heappop(start_heap)
                #print(f'start_heap: {start_heap}')
                cost+=val
                if left<=right:
                    heapq.heappush(start_heap, (costs[left], left))
                    left+=1
            elif (len(start_heap)>0 and len(end_heap) > 0) and (end_heap[0][0] < start_heap[0][0]):
                #print(f'taking from end_heap')
                val, _ = heapq.heappop(end_heap)
                #print(f'end_heap: {end_heap}')
                cost+=val
                if left <= right:
                    heapq.heappush(end_heap, (costs[right], right))
                    right-=1
            else:
                if len(start_heap)>0:
                    val, _ = heapq.heappop(start_heap)
                    cost+=val
                    if left<=right:
                        heapq.heappush(start_heap, (costs[left], left))
                        left+=1
                if len(end_heap)>0:
                    val, _ = heapq.heappop(end_heap)
                    cost+=val
                    if left <= right:
                        heapq.heappush(end_heap, (costs[right], right))
                        right-=1

            k-=1
        return cost






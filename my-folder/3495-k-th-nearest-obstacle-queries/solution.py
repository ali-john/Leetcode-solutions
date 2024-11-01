class Solution:
    def resultsArray(self, q: List[List[int]], k: int) -> List[int]:
        n = len(q)
        ans = [-1]*n

        heap = []

        for i, (x,y) in enumerate(q):
            d = abs(x)+abs(y)

            if len(heap)<k:
                heapq.heappush(heap,-d)
            elif -heap[0]>d:
                heapq.heappushpop(heap,-d)

            if len(heap)==k:
                ans[i] = -heap[0]
        return ans
                
            

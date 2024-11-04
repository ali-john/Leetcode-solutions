class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        heap = []

        left = 0
        ans = []
        for i in range(k):
            heapq.heappush(heap,(-nums[i],i))

        ans.append(-heap[0][0])

        for right in range(k,n):
            left+=1
            heapq.heappush(heap,(-nums[right],right))

            while True and heap:
                val,index = heap[0]
                if index>=left and index<=right:
                    ans.append(-val)
                    break
                else:
                    heapq.heappop(heap)
        return ans





            
            


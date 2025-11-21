class Solution:
    def findMaxSum(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        n = len(nums1)

        vals = defaultdict(list)
        for a, b in zip(nums1, nums2):
            vals[a].append(b)
        
        heap = []
        per_val_ans = {}
        curr_sum = 0
        unique_vals = sorted(vals.keys())
        for v in unique_vals:
            before_sum = curr_sum
            for x in vals[v]:
                if len(heap) < k:
                    curr_sum+=x
                    heapq.heappush(heap, x)
                else:
                    if heap[0] < x:
                        smallest = heapq.heappop(heap)
                        curr_sum-=smallest
                        curr_sum+=x
                        heapq.heappush(heap, x)
            per_val_ans[v] = before_sum
        ans = [per_val_ans[a] for a in nums1]
        return ans

                

        

        
        
    

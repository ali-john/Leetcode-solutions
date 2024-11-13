class Solution:
    def mostFrequentIDs(self, nums: List[int], freq: List[int]) -> List[int]:
        n = len(nums)
        table = defaultdict(int)

        ans = []
        maxHeap = []

        for i in range(n):
            table[nums[i]]+= freq[i]
            heapq.heappush(maxHeap,(-table[nums[i]],nums[i]))
            
            while table[maxHeap[0][1]]< -maxHeap[0][0]:
                heapq.heappop(maxHeap)
            ans.append(-maxHeap[0][0])
        return ans


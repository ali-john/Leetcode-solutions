class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        total = 0
        window_start = 0
        window_end = k
        total = sum(nums[0:k])
        ans = total/k

        if k>=len(nums):
            return sum(nums)/len(nums)

        while window_end<len(nums):
            total+=nums[window_end]
            total-=nums[window_start]
            ans = max(ans,(total/k))
            window_end+=1
            window_start+=1
        return ans




        

        



        

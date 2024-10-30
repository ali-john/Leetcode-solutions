class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        
        # Compute the number of subarrays with sum exactly equal to the goal by subtracting the count of 
        # subarrays with sum ≤ goal - 1 from the count of subarrays with sum ≤ goal.

        def getsum(goal):
            n = len(nums)
            left = 0
            total = 0
            total_sum = 0

            for right in range(n):
                total_sum+=nums[right]

                while total_sum>goal and left<=right:
                    total_sum-=nums[left]
                    left+=1
                
                total+=(right-left+1)
            return total
        
        return getsum(goal) - getsum(goal-1) 

    



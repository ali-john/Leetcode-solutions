class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        """
        Maintain a constant window of length k and look for maximum sum
        """
        n = len(nums)
        table = Counter(nums[0:k])
        left = 0
        max_sum = 0
        curr_sum = sum(nums[0:k])
        
        if len(table)==k:
            max_sum = max(max_sum,curr_sum)
        for right in range(k,n):
            curr_sum += nums[right]
            curr_sum-=nums[left]

            table[nums[right]]+=1
            table[nums[left]]-=1
            if table[nums[left]]<=0:
                del table[nums[left]]
            
            if len(table)==k:
                max_sum = max(max_sum,curr_sum)
    
            left+=1

        return max_sum
                

            




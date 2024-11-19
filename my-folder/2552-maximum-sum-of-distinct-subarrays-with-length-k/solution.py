class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        """
        Maintain a constant window of length k and look for maximum sum
        """
        table = defaultdict(int)
        n = len(nums)
        left = 0

        curr_sum = 0
        max_sum = 0
        for right in range(n):
            curr_sum+=nums[right]

            table[nums[right]]+=1

            if right>=k:
                table[nums[left]]-=1
                curr_sum-=nums[left]
                if table[nums[left]]==0:
                    del table[nums[left]]
                left+=1
            
            if len(table)==k:
                max_sum = max(curr_sum,max_sum)
        return max_sum







class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:

        prefix_sum = 0
        remainder_dict = {0: 0}
        max_sum = float('-inf')
        
        for i, num in enumerate(nums):
            prefix_sum += num
            remainder = (i+1) % k
            
            if remainder in remainder_dict:
                prev_sum = remainder_dict[remainder]
                subarr_sum = prefix_sum - prev_sum
                max_sum = max(max_sum, subarr_sum)
            # update sum
            if remainder in remainder_dict:
                remainder_dict[remainder] = min(prefix_sum,remainder_dict[remainder])
            else:
                remainder_dict[remainder] = prefix_sum
            
        return max_sum

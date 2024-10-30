class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        left = 0
        product = 1
        total = 0

        for right in range(n):
            product*=nums[right]

            while product>=k and left<=right:
                total+=(n-right)
                product = product//nums[left]
                left+=1
        total_subarrays = (n*(n+1))//2
        return (total_subarrays - total)




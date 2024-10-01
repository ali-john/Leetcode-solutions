class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        n = len(nums)
        min_diff = float("inf")
        max_curr = nums[k-1]
        min_curr = nums[0]
        min_diff = min(min_diff,(max_curr-min_curr))

        left = 0
        for right in range(k,n):
            max_curr = nums[right]
            left+=1
            min_curr = nums[left]
            min_diff = min(min_diff,(max_curr-min_curr))
        
        return min_diff


class Solution:
    def countElements(self, nums: List[int], k: int) -> int:
        if k == 0:
            return len(nums)
        n = len(nums)
        nums.sort()
        threshold = nums[n - k]

        return bisect_left(nums,threshold)

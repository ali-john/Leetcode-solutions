class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k%n

        stack = nums[:n-k]
        last = nums[-k:]

        nums[:k] = last
        nums[k:] = stack
        


class Solution:
    def absDifference(self, nums: List[int], k: int) -> int:
        n = len(nums)
        inc = sorted(nums)
        dec = sorted(nums, reverse = True)

        return abs(sum(inc[:k]) - sum(dec[:k]))

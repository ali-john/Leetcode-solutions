class Solution:
    def maxKDistinct(self, nums: List[int], k: int) -> List[int]:
        s = list(set(nums))
        s.sort(reverse=True)
        return s[:k]


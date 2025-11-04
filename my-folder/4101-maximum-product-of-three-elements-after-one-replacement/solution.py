class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        abs_arr = [abs(num) for num in nums]
        max_1 = max(abs_arr)
        abs_arr.remove(max_1)
        max_2 = max(abs_arr)
        if max_1 == 0 or max_2==0: return 0
        return max_1 * max_2 * 100000

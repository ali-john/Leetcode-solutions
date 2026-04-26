class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        n = len(nums)

        lengths = [1]*n
        for i in range(n-2, -1, -1):
            if nums[i] < nums[i+1]:
                lengths[i] = lengths[i+1] + 1

        def is_possible(k):
            for i in range(n):
                if lengths[i] >= k:
                    if i + k < n:
                        if lengths[i+k] >= k:
                            return True
            return False

        left = 1
        right = (n//2) + 1
        ans = -1
        while left <= right:
            mid = (left + right) // 2
            if is_possible(mid):
                ans = max(ans, mid)
                left = mid + 1
            else:
                right = mid - 1
        return ans

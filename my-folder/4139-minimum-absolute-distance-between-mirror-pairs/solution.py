class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        d = defaultdict(int)
        n, ans = len(nums), inf
        nums = [str(num) for num in nums]

        for i in range(n - 1, -1, -1): 
            rev = nums[i][::-1].lstrip('0')
            if rev in d: 
                ans = min(ans, d[rev] - i)
            d[nums[i]] = i

        return -1 if ans == inf else ans

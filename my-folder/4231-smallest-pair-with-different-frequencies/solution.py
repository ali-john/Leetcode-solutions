class Solution:
    def minDistinctFreqPair(self, nums: list[int]) -> list[int]:
        c = Counter(nums)
        nums = sorted(nums)
        ans = [nums[0]]
        for num in nums:
            if num!=nums[0] and c[num]!=c[nums[0]]:
                ans.append(num)
                break
        return ans if len(ans) == 2 else [-1, -1]



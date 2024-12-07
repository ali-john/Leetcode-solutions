class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        window = Counter()
        left = 0
        ans = 0

        for right in range(n):
            window[nums[right]]+=1

            while abs(max(window) - min(window))>2:
                if window[nums[left]]==1:
                    del window[nums[left]]
                else:
                    window[nums[left]]-=1
                left+=1
            ans += (right-left+1)
        return ans

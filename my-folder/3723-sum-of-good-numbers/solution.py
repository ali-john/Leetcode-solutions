class Solution:
    def sumOfGoodNumbers(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = 0

        for i in range(n):
            prev = i-k
            next_ = i+k
            if prev>=0 and next_ <n:
                if nums[i]>nums[prev] and nums[i]>nums[next_]:
                    ans+=nums[i]
            elif prev>=0 and next_ >=n:
                if nums[i]>nums[prev]:
                    ans+=nums[i]
            elif prev<0 and next_ <n:
                if  nums[i]>nums[next_]:
                    ans+=nums[i]
        return ans


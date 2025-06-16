class Solution:
    def maximumProduct(self, nums: List[int], m: int) -> int:
        n = len(nums)

        pos = float('-inf')
        neg = float('inf')
        ans = float('-inf')

        if m == 1:
            return max(num*num for num in nums)

        for j in range(m-1,n):
            i = j - (m - 1)
            x = nums[i]

            pos = max(pos,x)
            neg = min(neg,x)

            ans = max(ans, neg*nums[j], pos*nums[j])
        return ans




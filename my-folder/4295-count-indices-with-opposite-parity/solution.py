class Solution:
    def countOppositeParity(self, nums: list[int]) -> list[int]:
        n = len(nums)
        ans = [0]*n
        for i in range(n):
            parity = 0
            for j in range(i+1, n):
                if (nums[j]%2) != (nums[i]%2):
                    parity+=1
            ans[i] = parity
        return ans


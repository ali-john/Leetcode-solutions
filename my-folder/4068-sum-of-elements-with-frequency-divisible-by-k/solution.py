class Solution:
    def sumDivisibleByK(self, nums: List[int], k: int) -> int:
        table = Counter(nums)
        ans = 0
        for key,val in table.items():
            if val%k == 0:
                ans+=(key*val)
        return ans

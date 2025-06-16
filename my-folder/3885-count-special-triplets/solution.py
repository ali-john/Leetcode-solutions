class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        right = Counter(nums)
        left = Counter()
        ans = 0

        for num in nums:
            right[num]-=1
            t = num*2

            ans = (ans + (right[t]*left[t])) % MOD

            left[num]+=1
        
        return ans




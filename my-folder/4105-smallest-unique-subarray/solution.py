class Solution:
    def smallestUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        BASE = 911382323
        MOD = 10**18 + 3

        powers = [1] * (n + 1)
        for i in range(1, n + 1):
            powers[i] = (powers[i - 1] * BASE) % MOD
        

        def is_possible(k):
            freq = defaultdict(int)
            # first window
            h = 0
            for i in range(k):
                h = (h*BASE + nums[i])%MOD
            freq[h]+=1
            # remaining windows:
            for i in range(k,n):
                left = nums[i - k]
                h = (h - left*powers[k - 1])%MOD
                # add new right char
                h = (h*BASE + nums[i])%MOD
                freq[h]+=1
            
            for count in freq.values():
                if count == 1:
                    return True

            return False

        left, right = 1, n
        ans = n

        while left <= right:
            mid = (left + right) // 2

            if is_possible(mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1

        return ans

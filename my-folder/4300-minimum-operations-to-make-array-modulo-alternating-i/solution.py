class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:

        n = len(nums)

        if n == 1:
            return 0

        ans = float('inf')

        for x in range(k):
            for y in range(k):
                if x == y:
                    continue

                curr_total = 0

                for index, curr in enumerate(nums):
                    r = curr % k
                    target = x if index % 2 == 0 else y

                    incre_ops = (target - r) % k
                    decre_ops = (r - target) % k

                    curr_total += min(incre_ops, decre_ops)

                ans = min(ans, curr_total)

        return ans
        

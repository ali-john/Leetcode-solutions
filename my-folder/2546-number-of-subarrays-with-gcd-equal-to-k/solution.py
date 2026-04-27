class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        n = len(nums)
        #. --- Optimal
        # check this article: https://discuss.codechef.com/t/ksizegcd-editorial/104879
        prev = {}
        ans = 0
        for x in nums:
            curr = defaultdict(int)
            curr[x] += 1

            for g, cnt in prev.items():
                new_gcd = gcd(g, x)
                curr[new_gcd]+=cnt
            if k in curr:
                ans+= curr[k]
            prev = curr
        return ans





        # Brute force solution
        # ans = 0

        # for i in range(n):
        #     if nums[i] == k:
        #         ans+=1
        #     curr_gcd = nums[i]
        #     for j in range(i+1, n):
        #         curr_gcd = gcd(curr_gcd, nums[j])
        #         if curr_gcd == k:
        #             ans+=1
        # return ans



class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        nums = set(nums)
        n = len(nums)

        table = defaultdict()
        ans = 0
        for num in nums:
            x = table.get(num - 1, 0 )
            y = table.get(num +1, 0)
            val = x + y + 1
            table[num - x] = val
            table[num + y] = val
            ans = max(val,ans)
        return ans


       


        

        # sol 2

        # nums = set(nums)

        # if len(nums) == 0:
        #     return 0
        # ans = float("-inf")

        # for num in nums:
        #     length = 1
        #     if num - 1 not in nums:
        #         while num + length in nums:
        #             length+=1
        #     ans = max(length,ans)
        # return ans
        


        

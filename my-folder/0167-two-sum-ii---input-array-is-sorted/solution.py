class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        lo = 0
        hi = n - 1

        ans = []
        while lo < hi:
            if nums[lo] + nums[hi] == target:
                ans.append(lo+1)
                ans.append(hi+1)
                return ans
            if nums[lo] + nums[hi] > target:
                hi-=1
            else:
                lo +=1
        return [-1,-1]

        
        
        
        
        # n = len(nums)
        # table = defaultdict(list)

        # for i, num in enumerate(nums):
        #     table[num].append(i)
        
        # ans = []
        # for i, num in enumerate(nums):
        #     second = target - num
        #     if second in table:
        #         if second == num:
        #             if len(table[num]) > 1:
        #                 ans.append(table[num].pop()+1)
        #                 ans.append(table[num].pop()+1)
        #                 break
        #         else:
        #             ans.append(i+1)
        #             ans.append(table[second].pop()+1)
        #             break
        # return sorted(ans)
        
        

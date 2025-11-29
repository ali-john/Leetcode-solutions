class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        ans = []
        vals = SortedList()
        for i, num in enumerate(nums):
            vals.add(num)
            if i >=k: vals.remove(nums[i-k])
            if i>=k - 1: ans.append(min(0, vals[x - 1]))
        return ans
        
        
        
        
        
        
        
        
        
        
        
        
        # n = len(nums)
        # table = defaultdict(list)
        # for i in range(k):
        #     table[nums[i]].append(i)
        
        # ans = []
        
        # # for window 0
        # def get_xsmallest():
        #     temp = x
        #     x_smallest = 0
        #     for num in range(-50,0):
        #         if num in table:
        #             temp-= len(table[num])
        #             if temp <= 0:
        #                 x_smallest = num
        #                 break
        #     return x_smallest
        # ans.append(get_xsmallest())
        # # start from window 1 onwards
        # for i in range(k, n):
        #     to_add = nums[i]
        #     to_remove = nums[i - k]
        #     table[to_add].append(i)
        #     table[to_remove].pop()
        #     if len( table[to_remove]  ) == 0:
        #         del table[to_remove]
        #     x_smallest = get_xsmallest()
        #     ans.append(x_smallest)
        # return ans

                    
                
        



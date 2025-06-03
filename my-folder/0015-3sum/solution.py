class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums = sorted(nums)
        
        output = []
        def twoSum(target, index):
            left = index
            right = n - 1

            while left < right:
                s = nums[left] + nums[right]

                if s == target:
                    output.append([nums[left], nums[right], -target])
                    left+=1
                    right -=1

                    while left<right and nums[left] == nums[left - 1]: left+=1
                    while left<right and nums[right] == nums[right+1]: right-=1
                
                elif s > target:
                    right-=1
                else:
                    left+=1
            return
        
        for i in range(n):
            if i>0 and nums[i] == nums[i-1]: continue
            twoSum(-nums[i],i+1)
        return output






        
        
        
        
        
        
        
        
        
        
        # n = len(nums)
        # table = defaultdict(int)
        # nums = sorted(nums)
        # output = []


        # def two_sum(target,z_index):
        #     left = z_index
        #     right = n - 1

        #     while left<right:
        #         total = nums[left] + nums[right]
        #         if total == target:
        #             output.append([nums[left],nums[right],-target])

        #             left+=1
        #             right-=1
        #             while left<right and nums[left]==nums[left-1]: left+=1
        #             while left<right and nums[right]==nums[right+1]: right-=1
        #         elif total>target:
        #             right-=1
        #         else: left+=1
        #     return
        
        # for i in range(n):
        #     if i>0 and nums[i]==nums[i-1]: continue
        #     two_sum(-nums[i],i+1)
        # return output
        
        


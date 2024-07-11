class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        

        def closestSum(n1,start):
            end = len(nums)-1
            nonlocal difference 
            nonlocal closest_sum 
            while start<end:
                s = nums[start]
                e = nums[end]
                total = s+e+n1

                if abs(total - target)<difference:
                    difference = abs(total-target)
                    closest_sum = total
                    
                if total>target:
                    end-=1
                else:
                    start+=1
                
            return

        nums = sorted(nums)
        difference = float("inf")
        closest_sum = float("inf")
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]: # remove duplicates
                continue
            
            closestSum(nums[i],i+1)
        return closest_sum




        

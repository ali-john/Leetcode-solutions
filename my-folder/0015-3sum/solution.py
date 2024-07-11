class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        def TwoSum(target,start):
            
            end = len(nums)-1

            while start<end:
                total = nums[start]+nums[end]

                if total ==target:
                    triplets.append([-target,nums[start],nums[end]])
                    start+=1
                    end-=1
                
                    while start<end and nums[start] == nums[start-1]:
                        start+=1
                    while start<end and nums[end]==nums[end+1]:
                        end-=1

                elif total>target:
                    end-=1
                else:
                    start+=1
            return

        nums = sorted(nums)
        triplets = []
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue # skip duplicates
            TwoSum(-nums[i],i+1)
        return triplets

        
        
    






        



        

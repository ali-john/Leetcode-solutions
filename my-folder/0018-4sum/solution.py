class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def TwoSum(previous_sum, start):
            end = len(nums)-1
            while start<end:
                total = sum(previous_sum)+nums[start]+nums[end]
                if total == target:
                    quads.append([previous_sum[0],previous_sum[1],nums[start],nums[end]])
                    start+=1
                    end-=1
                    while start<end and nums[start]==nums[start-1]:
                        start+=1
                    while start<end and nums[end]==nums[end+1]:
                        end-=1
                elif total<target:
                    start+=1
                else:
                    end-=1
            return
        nums = sorted(nums)
        quads = []

        for i in range(len(nums)-3):
            if i>0 and nums[i]==nums[i-1]:
                continue
            for j in range(i+1,len(nums)-2):
                if j>i+1 and nums[j]==nums[j-1]:
                    continue
                TwoSum([nums[i],nums[j]],j+1)
        return quads
            

        

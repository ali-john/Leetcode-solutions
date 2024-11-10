class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        n = len(nums)

        def check(arr):
            for i in range(1,len(arr)):
                if arr[i]>arr[i-1]:
                    continue
                else:
                    return False
            return True
            
        for i in range((n-(2*k))+1):
            arr1 = nums[i:i+k]
            arr2 = nums[i+k:i+2*k]
            # print(arr1)
            # print(arr2)
            if check(arr1) and check(arr2):
                return True
        return False

            
            
            

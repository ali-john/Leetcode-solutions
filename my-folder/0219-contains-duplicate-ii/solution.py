class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        output = False
        for i in range(len(nums)-1):
            if i+k<=len(nums):
                sub_arr = nums[i+1:(i+k)+1]
                #print(sub_arr)
                if nums[i] in sub_arr:
                    output=True
                    break
            else:
                sub_arr = nums[i+1:len(nums)]
                if nums[i] in sub_arr:
                    output = True
                    break
        return output

        

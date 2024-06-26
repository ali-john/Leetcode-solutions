class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 0
        
        nums.append(-999999999999)
        nums.insert(0,-999999999999)
        def find_peak():
            left = 0
            right = len(nums)-1
            while left<=right:
                mid = (left+right)//2

                left_num = nums[mid-1]
                right_num = nums[mid+1]
                if left_num< nums[mid] > right_num:
                    return mid
                
                elif left_num<right_num:
                    left = mid+1
                else:
                    right = mid-1
        
        return find_peak()-1
        



        

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        def find_index():
            left = 0
            right = len(nums)-1
            index_to_be = 0
            while left<=right:
                mid = (left+right)//2
                number = nums[mid]

                if number==target:
                    return mid
                
                elif number>target:
                    right = mid-1
                    index_to_be = mid
                elif number<target:
                    left = index_to_be = mid+1
            return index_to_be

        output = find_index()
        return output




            




        

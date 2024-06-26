class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums)==1:
            return 0 if target==nums[0] else -1
        pivot_point = 0


        def find_pivot():
            left = 0
            right = len(nums)-1

            while left<right:
                mid = (left+right)//2

                if nums[mid]>nums[right]:
                    left = mid+1
                else:
                    right = mid
            return left
                
        def search_now(left,right):

            while left<=right:
                mid = (left+right)//2
                if nums[mid] == target:
                    return mid
                
                elif nums[mid]<target:
                    left = mid+1
                else:
                    right = mid-1
            
            return -1

        pivot = find_pivot()
        if nums[pivot]<=target<=nums[-1]:
            return search_now(pivot,len(nums)-1)
        else:
            return search_now(0,pivot-1)
    
        
                

                

        

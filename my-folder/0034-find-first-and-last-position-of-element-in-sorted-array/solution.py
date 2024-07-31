class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def search(find_max_index):
            index = -1
            start = 0
            end = len(nums)-1

            while start<=end:
                middle = (start+end)//2
                if nums[middle]<target:
                    start = middle+1
                elif nums[middle]>target:
                    end = middle -1
                
                else:
                    index = middle
                    if find_max_index:
                        start = middle+1
                    else:
                        end = middle -1
            return index


        result = [-1,-1]
        result[0] = search(False)
        if result[0]!=-1:
            result[1] = search(True)
        
        return result
        
        
            


        
            

                


        

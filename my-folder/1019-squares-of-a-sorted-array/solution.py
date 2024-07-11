class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        output = [0 for val in range(len(nums))]
        squareIndex = len(nums)-1

        end = len(nums)-1
        start = 0

        while start<=end:
            start_s = nums[start]**2
            end_s = nums[end]**2

            if start_s>end_s:
                output[squareIndex] = start_s
                start+=1
            else:
                output[squareIndex]= end_s
                end-=1
            squareIndex-=1
        return output


        





        

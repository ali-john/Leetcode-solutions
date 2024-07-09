class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        output = float("-inf")

        window_start = 0
        window_end= 0
        maxOnesOccurances = 0
        while window_end<len(nums):
            endChr = nums[window_end]
            if endChr ==1:
                maxOnesOccurances+=1
            
            if (window_end - window_start+1 - maxOnesOccurances> k ):
                if nums[window_start]==1:
                    maxOnesOccurances-=1
                window_start+=1
                
            output = max(output,window_end-window_start+1)
            window_end+=1
        return output






        

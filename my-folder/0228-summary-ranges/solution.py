class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        n = len(nums)

        output = []

        i = 0
        while i < n:
            start = i
            while start+1 < n and nums[start+1] == nums[start]+1:
                start+=1
            
            if start == i:
                output.append(str(nums[i]))
                i+=1
            else:
                output.append(f'{nums[i]}->{nums[start]}')
                i = start+1
            
        
        return output



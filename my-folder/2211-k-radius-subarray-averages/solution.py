class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)


        output = [-1]*n
        if n//2<k:
            return output
        left = 0
        right = 2*k
        total_sum = sum(nums[left:right])


        for i in range(k,n-k):
            total_sum+=nums[right]
            output[i] = total_sum // (2*k+1)
            total_sum-=nums[left]
            left+=1
            right+=1
            
            
        return output


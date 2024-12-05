class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        n = len(nums)
        possibles = []

        for i in range(n):
            for j in range(i,n):
                if (j-i+1)>=l and (j-i+1)<=r:
                    possibles.append(nums[i:j+1])

        #print(possibles)
        ans  = float('inf')
        for sub in possibles:
            if sum(sub)>0:
                ans = min(ans,sum(sub))
        if ans==float('inf'):
            return -1
        else:
            return ans
        

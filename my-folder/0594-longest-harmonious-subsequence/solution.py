class Solution:
    def findLHS(self, nums: List[int]) -> int:
        count = collections.Counter(nums)
        ans = 0
        for num,freq in count.items():
            if num+1 in count:
                ans = max(ans,freq+count[num+1])
        return ans









        


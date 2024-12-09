class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        

        n = len(nums)
        q_n = len(queries)

        prefix = [0]*n

        for i in range(1,n):
            if nums[i]%2==nums[i-1]%2:
                prefix[i] = prefix[i-1]+1
            
            else:
                prefix[i] = prefix[i-1]
        
        ans = [True]*q_n

        for i in range(q_n):
            query = queries[i]
            start = query[0]
            end = query[1]
            if prefix[start]!=prefix[end]:
                ans[i] = False
        return ans



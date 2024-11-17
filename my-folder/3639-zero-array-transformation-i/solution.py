class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n = len(nums)
        q = len(queries)
        range_arr = [0]*(n+1)

        for i in range(q):
            start,end = queries[i]
            range_arr[start]-=1
            if end+1>n:
                range_arr[n-1]+=1
            else:
                range_arr[end+1]+=1

        prev = range_arr[0]
        for i in range(1,n):
            prev+=range_arr[i]
            range_arr[i] = prev

        for i in range(n):
            nums[i] = nums[i] + range_arr[i]
            if nums[i]>0:
                return False
        return True

                

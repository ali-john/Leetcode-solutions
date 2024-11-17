class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:

        def is_possible(val):
            temp_nums = nums[:]
            n = len(nums)
            q = val
            range_arr = [0]*(n+1)
    
            for i in range(q):
                start,end, value = queries[i]
                range_arr[start]-=value
                if end+1>n:
                    range_arr[n-1]+=value
                else:
                    range_arr[end+1]+=value
    
            prev = range_arr[0]
            for i in range(1,n):
                prev+=range_arr[i]
                range_arr[i] = prev
    
            for i in range(n):
                temp_nums[i] = temp_nums[i] + range_arr[i]
                if temp_nums[i]>0:
                    return False
            return True


        #print(is_possible(1))
        all_zero = True
        for i in range(len(nums)):
            if nums[i]>0:
                all_zero = False
        if all_zero:
            return 0
        
        left = 1
        right = len(queries)

        k = 1000000000

        while left<=right:
            mid = (left+right)//2
            if is_possible(mid):
                k = min(k,mid)
                right = mid -1
            else:
                left = mid+1
        if k==1000000000:
            return -1
        else:
            return k
        

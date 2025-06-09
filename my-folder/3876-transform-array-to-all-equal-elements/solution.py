class Solution:
    def canMakeEqual(self, nums: List[int], k: int) -> bool:
        n = len(nums)

        # make 1s

        i = 0
        ops = 0
        copy_arr = nums[:]
        while i < n:
            if i+1 < n and copy_arr[i] == -1:
                copy_arr[i] = 1
                copy_arr[i+1]*=-1
                ops+=1
            i+=1
        
        if ops<=k and all(num ==1 for num in copy_arr): return True

        # make all -1s
        i = 0
        ops = 0
        copy_arr = nums[:]
        while i < n:
            if i+1 < n and copy_arr[i] == 1:
                copy_arr[i] = -1
                copy_arr[i+1]*=-1
                ops+=1
            i+=1
        
        if ops<=k and all(num ==-1 for num in copy_arr): return True

        return False




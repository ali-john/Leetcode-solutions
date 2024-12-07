class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:

        n = len(nums)
        if n==1:
            if nums[0]==k:
                return 0
            elif k>nums[0]:
                return -1
            else:
                return 1
        count  = 0
        def is_valid():
            for num in nums:
                if num!=k:
                    return False
            return True
        def is_same():
            p = set()
            for num in nums:
                p.add(num)
            if len(p)==1:
                return True
            else:
                return False
            
        while True:
            valid_int = -1

            if is_same() and k<nums[0]:
                return count+1
            elif is_same() and k==nums[0]:
                return 0
                
            for i in range(1,max(nums)+1):
                s = set()
                for j in range(n):
                    if nums[j]>i:
                        s.add(nums[j])
                if len(s)==1:
                    count+=1
                    valid_int = i
                    for j in range(n):
                        if nums[j]>valid_int:
                            nums[j] = valid_int
                    if is_same():
                        if k<nums[0]:
                            return count+1
                if is_valid():
                    return count
            if not is_valid() and valid_int==-1:
                return -1
       
           
               
           
            
        

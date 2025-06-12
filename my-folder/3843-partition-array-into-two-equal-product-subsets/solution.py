class Solution:
    def checkEqualPartitions(self, nums: List[int], target: int) -> bool:


        n = len(nums)
        s = []
        
        def f(i,p, path):
            if p == target:
                return path

            if i>=n or (p> target):
                return None

            res = f(i+1,p,path)
            if res is not None:
                return res

            return f(i+1,p*nums[i], path+ [nums[i]])

        ans = f(0,1,[])
        p = 1
        for num in nums:
            if num > target:
                return False
            p*=num

        if p == target*target:
            if not ans is None:
                if len(ans)!=n:
                    return True
                else:
                    return False
            else:
                return False
            
    
        else:
            return False
            

        
        

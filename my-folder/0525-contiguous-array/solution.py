class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        table = {}
        table[0] = -1

        total = 0
        c = 0
        for i in range(n):
            if nums[i]==0:
                total-=1
            else:
                total+=1
            
            if table.get(total) is not None:
                c = max(c,i-table.get(total))
            else:
                table[total] = i
        return c

            
        
    



            
        
        

class Solution:
    def countValidSelections(self, nums: List[int]) -> int:

        def simulate(start,direction):
            n = len(nums)
            nums_copy = nums[:] 
            curr = start
            move = direction
            
            while 0 <= curr < n:
                if nums_copy[curr] == 0:
                    curr += move
                elif nums_copy[curr] > 0:
                    nums_copy[curr] -= 1
                    move = -move 
                    curr += move
    
            return all(x == 0 for x in nums_copy)


        n = len(nums)
        count = 0
        
        for i in range(n):
            if nums[i] == 0:
                if simulate(i,-1):
                    count+=1
                if simulate(i,1):
                    count+=1
        return count

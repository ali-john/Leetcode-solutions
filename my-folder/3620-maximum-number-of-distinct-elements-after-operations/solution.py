class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        nums.sort()  
        taken = set() 
        next_ = float('-inf')  
    
        for num in nums:
            possible = max(next_, num - k)
            if possible <= num + k:
                taken.add(possible)
                next_ = possible + 1 
    
        return len(taken)

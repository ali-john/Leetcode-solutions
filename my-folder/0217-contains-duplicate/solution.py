class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        table = defaultdict(int)
        for num in nums:
            table[num]+=1
        
        for key,val in table.items():
            if val>1:
                return True
        return False

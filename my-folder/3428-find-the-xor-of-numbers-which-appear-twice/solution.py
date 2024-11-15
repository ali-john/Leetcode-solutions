class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:

        table = Counter(nums)
        doubles = []
        for key,val in table.items():
            if val>=2:
                doubles.append(key)
        if len(doubles)>0: 
            ans = doubles[0]  
        else: return 0
        
        for i in range(1,len(doubles)):
            ans^=doubles[i]
        return ans

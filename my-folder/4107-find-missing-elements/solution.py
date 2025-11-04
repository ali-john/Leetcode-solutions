class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        table = defaultdict(int)
        for num in nums:
            table[num]+=1

        min_ = min(nums)
        max_ = max(nums)
        ans = []
        for num in range(min_,max_):
            if num not in table:
                ans.append(num)
        return ans
                
            

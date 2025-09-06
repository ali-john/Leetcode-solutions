class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        n = len(queries)
        ans = [-1]*n
        table = defaultdict(int)
        occurance = 0

        for i,num in enumerate(nums):
            if num == x:
                occurance+=1
                table[occurance] = i
        
        for i,query in enumerate(queries):
            if query in table:
                ans[i] = table[query]
        return ans


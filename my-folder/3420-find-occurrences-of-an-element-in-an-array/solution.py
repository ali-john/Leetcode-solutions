class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        table = defaultdict(int)
        n = len(queries)
        output = [-1]*n
        count = 0
        for i,num in enumerate(nums):
            if num==x:
                count+=1
                table[count]=i
        for i,q in enumerate(queries):
            if q<=count:
                output[i] = table[q]
        return output
        


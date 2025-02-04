class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        n = len(nums)
        table = defaultdict(int)

        for num in nums:
            table[num]+=1
        
        def check(val):
            curr = 0
            max_curr = 0
            for i,num in enumerate(nums):
                if num==k: curr-=1
                elif num==val: curr+=1

                if curr<0:
                    curr = 0
                max_curr = max(curr,max_curr)
            return max_curr
            
        # brute force on each number in range 1 <=50
        ans = table[k]
        other = 0
        for i in range(1,51):
            if i in table:
                other = max(other,check(i))
        return other+ans
            



class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        prefix_arr = [0]*n
        table = defaultdict(int)
        table[0] = -1
        prev = 0
        for i in range(n):
            prev = (prev + nums[i])%k
            if prev in table:
                if i - table[prev]>1:
                    return True
            else:
                table[prev] = i
        return False



        

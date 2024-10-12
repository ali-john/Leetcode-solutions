class Solution:
    def maxGoodNumber(self, nums: List[int]) -> int:
        max_num = 0
        for p in permutations(nums):
            n1 = bin(p[0])[2:]
            n2 = bin(p[1])[2:]
            n3 = bin(p[2])[2:]
            max_num = max(max_num, int(n1+n2+n3,2))
        return max_num

    
       

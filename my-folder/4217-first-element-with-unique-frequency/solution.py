class Solution:
    def firstUniqueFreq(self, nums: List[int]) -> int:
        c = Counter(nums)  # {20:2, 30:3, 40:2}
        freq = defaultdict(int) # {2:2, 4:1, 5: 7} etc
        for _,val in c.items():
            freq[val]+=1
        
        for i in range(len(nums)):
            num = nums[i]
            if freq[c[num]] == 1:
                return num
        return -1




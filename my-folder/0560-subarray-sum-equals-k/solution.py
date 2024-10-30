class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        table = Counter()

        table[0] = 1
        cum = 0
        total = 0
        for i,num in enumerate(nums):
            cum+=num

            if cum-k in table:
                total+=(table[cum-k])
            table[cum]+=1
        return total



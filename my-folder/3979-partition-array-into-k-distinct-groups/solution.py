class Solution:
    def partitionArray(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        if k>n: return False
        groups = n%k
        if groups!=0: return False
        # check frequency

        table = Counter(nums)
        max_group = n//k

        for key,val in table.items():
            if val > max_group:
                return False
        
        return True

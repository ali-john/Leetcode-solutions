class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        n = len(nums)
        table = defaultdict(int)
        left = 0

        pairs_found, total = 0, 0 
        for right in range(n):
            if table[nums[right]]>=1:
                pairs_found+=table[nums[right]]
            table[nums[right]]+=1

            while pairs_found>=k:
                total+= n-right
                table[nums[left]]-=1

                if table[nums[left]]>=1:
                    pairs_found-= table[nums[left]]
                left+=1

        return total
        


class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        ans = 0

        for i in range(n):
            table = defaultdict(int)
            for j in range(i, n):
                table[nums[j]]+=1
                l = ( j - i + 1 ) // 2 
                if table[target] > 0 and table[target] > l:
                    #print(f'Table: {table}, i = {i}, j = {j}, l = {l}, ans = {ans}')
                    ans+=1
        return ans




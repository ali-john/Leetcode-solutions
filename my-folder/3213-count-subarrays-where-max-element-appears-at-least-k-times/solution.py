class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = 0
        m = max(nums)

        left, right = 0, 0
        table = defaultdict(int)
        while right < n:
            if nums[right] == m:
                table[m]+=1
            while left <= right and table[m] >= k:
                ans+=1
                right_count = n - right - 1
                ans+=right_count
                if nums[left] == m:
                    table[m]-=1
                left+=1
            right+=1
        return ans




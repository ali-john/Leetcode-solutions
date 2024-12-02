class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        n = len(nums)
        elements = Counter(nums)
        total = sum(nums)
        ans = float('-inf')

        for i in range(n):
            new_sum = total - nums[i]
            if new_sum%2!=0:
                continue
            else:
                element = new_sum//2
                if nums[i]==element and elements[element]>1:
                    ans = max(ans,nums[i])
                elif nums[i]!=element:
                    if element in elements:
                        ans = max(nums[i],ans)
        return ans
            

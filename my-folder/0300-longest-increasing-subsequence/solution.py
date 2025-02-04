class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # DP Solution
        # n = len(nums)
        # LIS = [1]*n

        # for i in reversed(range(n)):
        #     for j in range(i+1,n):
        #         if nums[j] > nums[i]:
        #             LIS[i] = max(LIS[i], 1 + LIS[j])

        # return max(LIS)

        # Binary Search for LIS: See at : https://youtu.be/OIU8ZLC4qIQ?si=kZxHyjND9QZjX3ll
        n = len(nums)
        sub = []
        for num in nums:
            i = bisect_left(sub,num)
            if i==len(sub): sub.append(num)
            else: sub[i] = num
        return len(sub)


            

            

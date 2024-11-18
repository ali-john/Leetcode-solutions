class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        n = len(nums)
        
        if n==1:
            return nums[0]
        
        freq = [0]*(max(nums)+1)
        print(freq)

        for num in nums:
            freq[num]+=num
        
        dp = [0]*len(freq)
        dp[1] = freq[1]

        for i in range(2,len(freq)):
            dp[i] = max(dp[i-1],freq[i]+dp[i-2])
        return dp[len(freq)-1]




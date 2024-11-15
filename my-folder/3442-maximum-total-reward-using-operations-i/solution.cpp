class Solution {
public:
    int solve(vector<int>& nums, int sum, int i,vector<vector<int>> &dp) {
        if (i >= nums.size()) {
            return sum;
        }
        if (dp[i][sum] != -1) {
            return dp[i][sum];
        }
        int ex = solve(nums, sum, i + 1,dp);
        int in = 0;
        if (nums[i] > sum) {
            in = solve(nums, sum + nums[i], i + 1,dp);
        }
        return dp[i][sum] = max(in, ex);
    }

    int maxTotalReward(vector<int>& nums) {
        sort(nums.begin(), nums.end());
          vector<vector<int>>dp(nums.size(),vector<int>(4001,-1));
        return solve(nums, 0, 0,dp);
    }
};

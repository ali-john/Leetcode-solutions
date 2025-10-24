class Solution {
public:
    int maxProduct(vector<int>& nums) {
        sort(nums.begin(),nums.end());
        int n = nums.size();
        int val1 = nums[n - 1];
        int val2 = nums[n-2];
        int ans = (val1 - 1) * (val2 - 1);
        return ans;
    }
};

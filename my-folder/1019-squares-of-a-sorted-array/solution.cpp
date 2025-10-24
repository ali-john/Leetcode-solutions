class Solution {
public:
    vector<int> sortedSquares(vector<int>& nums) {
        int n = nums.size();
        vector<int> ans;
        for (auto num:nums){
            ans.push_back(num*num);
        }
        sort(ans.begin(), ans.end());
        return ans;
    }
};

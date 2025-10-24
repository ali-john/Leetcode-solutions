class Solution {
public:
    int returnToBoundaryCount(vector<int>& nums) {
        int ans = 0;
        int sum = 0;

        for (auto num: nums)
        {
            sum+=num;
            if (sum == 0)
            {
                ans+=1;
            }
        }
        return ans;
    }
};

class Solution {
public:
    unordered_map<int,int> cache;
    int rob(vector<int>& nums) {
        if (nums.size()==0) return 0;
        if (nums.size()==1) return nums[0];
        cache.clear();
        int max1 = dp(nums,0,nums.size()-2);
        cache.clear();
        int max2 = dp(nums,1,nums.size()-1);
        return max(max1,max2);
    }
    int dp(vector<int>& nums,int start,int end)
    {
        if (start>end) return 0;
        if (cache.find(start)!=cache.end()) return cache[start];
        // dont rob the house
        int dont_rob = dp(nums,start+1,end);
        int rob_house = nums[start] + dp(nums,start+2,end);
        cache[start] = max(dont_rob,rob_house);
        return cache[start];

    }
};

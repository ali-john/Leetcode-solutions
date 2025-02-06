class Solution {
public:
    int longestSubarray(vector<int>& nums) {
        int max_num = *max_element(nums.begin(),nums.end());

        int i = 0;
        int ans = 1;
        while (i<nums.size())
        {   int length = 0;
            while ( i<nums.size() and nums[i] == max_num )
            {
                length+=1;
                i+=1;
            }
            ans = max(ans,length);
            i+=1;
        }
        return ans;
    }
};

class Solution {
public:
    int tupleSameProduct(vector<int>& nums) {
        unordered_map<int,int> table;

        for (int i=0; i<nums.size();i++)
        {
            for (int j=i+1;j<nums.size();j++)
            {
                int product = nums[i]*nums[j];
                table[product]+=1;
            }
        }
        int ans = 0;

        for (auto& pair:table)
        {
            int combinations = ( (pair.second)*(pair.second - 1) )/2;
            ans+=8*combinations;
        }
        return ans;
    }
};

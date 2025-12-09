class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> table;
        
        for (int i = 0; i < nums.size(); i++){
            int second = target - nums[i];
            if (table.find(second) != table.end() && table[second]!=i)
                return {table[second], i};
            table[nums[i]] = i;

        }
        return {};
    }
};

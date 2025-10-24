class Solution {
public:
    vector<int> getConcatenation(vector<int>& nums) {
        vector<int> out;
        for (auto num: nums){
            out.push_back(num);
        }
        for (auto num: nums){
            out.push_back(num);
        }
        return out;

    }
};

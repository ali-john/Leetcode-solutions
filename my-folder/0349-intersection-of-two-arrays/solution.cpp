class Solution {
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
        set<int> s;
        for (auto n: nums1){
            s.insert(n);
        }
        vector<int> ans;

        for (auto num: nums2){
            if (s.find(num) != s.end())
                ans.push_back(num);
                s.erase(num);
        }
        return ans;

    }
};

class Solution {
public:
    int maxProfitAssignment(vector<int>& difficulty, vector<int>& profit, vector<int>& worker) {
        vector<pair<int, int>> cost;
    for (int i = 0; i < (int)difficulty.size(); i++) {
        cost.push_back({difficulty[i], profit[i]});
    }

    int ans = 0;
    for (int w : worker) {
        int curr = 0;
        for (auto &c : cost) {
            if (c.first <= w)
                curr = max(curr, c.second);
        }
        ans += curr;
    }
    return ans;
    }
};

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int max_ans = INT_MIN;
        int min_val = INT_MAX;

        for (int i = 0; i< prices.size(); i++){
            if (prices[i] < min_val)
                min_val = prices[i];
            
            if ( ( prices[i] - min_val) > max_ans )
                max_ans = max(max_ans, prices[i] - min_val);
        }
        return max_ans;   

    }
};

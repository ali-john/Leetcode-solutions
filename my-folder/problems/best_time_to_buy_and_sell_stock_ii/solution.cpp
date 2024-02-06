class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int net_profit = 0;

        for (int i=0; i<prices.size()-1; i++)
        {
            int profit = prices[i+1] -  prices[i];
            if (profit>0)
            {
                net_profit+=profit;
            }
        }
        return net_profit;
        
    }
};
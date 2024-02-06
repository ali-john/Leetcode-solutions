class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int profit = 0;
        int min = prices[0];
        for (int i = 0;i<prices.size();i++)
        {
            if (prices[i]<min)
            {
                min = prices[i];
            }
            int diff = prices[i] - min;
            if (diff>profit)
            {
                profit = prices[i] - min;
            }
        }
        return profit;

        
    }
};
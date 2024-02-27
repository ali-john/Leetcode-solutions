class Solution {
public:
    int canCompleteCircuit(vector<int>& gas, vector<int>& cost) {
        int gas_sum = 0;
        int cost_sum = 0;
        for (int i=0;i<gas.size();i++)
        {
            gas_sum+=gas[i];
            cost_sum+=cost[i];
        }
        if (gas_sum>=cost_sum) // only cycle possible if cost is less than gas avaialble
        {
            int diff = -50; 
            bool in_cycle = false;
            int surplus = 0;
            int index = 0;
            for (int i=0;i<gas.size();i++)
            {
                int current_diff = gas[i]-cost[i];
                if ((current_diff)>=diff & (current_diff>0))
                {
                    if (!in_cycle)
                    {
                        diff = gas[i] - cost[i]; 
                        index = i;
                        in_cycle = true;
                    }
                    
                }
                if (in_cycle)
                {
                    surplus += (gas[i]-cost[i]);
                    if (surplus<0)
                    {
                        in_cycle = false;
                        surplus = 0;
                        diff = 0;
                    }
                }
            }
            return index;

        }
        else    return -1;


    }
};
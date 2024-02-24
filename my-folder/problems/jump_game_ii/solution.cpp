class Solution {

public:
    int jump(vector<int>& nums) {
        
        int steps = 0;
        int maxReach = 0;
        int currentPos = 0;
        int n = nums.size()-1;
        int i = 0;

        while (currentPos < n)
        {
            maxReach = max(maxReach, i + nums[i]);
            if (i==currentPos)
            {
                currentPos = maxReach;
                steps++;
            }
            i++;

        }
        return steps;



    }
    

    
    
};
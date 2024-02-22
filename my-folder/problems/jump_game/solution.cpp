class Solution {
public:
    
    

    bool canJump(vector<int>& nums) 
    {
        bool decision = false;
        
        int max= nums[0];
        for (int i=0;i<nums.size();i++)
        {
            if (max>=nums.size()-1)// we can reach till end
            {
                decision = true;
            }
            if (nums[i]==0 & max==i)
            {
                break;
            }
            if (nums[i]+i > max)
            {
                max = nums[i]+i;
            }
        }
        return decision;

    }
};
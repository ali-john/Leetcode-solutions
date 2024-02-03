class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        if (nums.size()==0)
        {
            return 0;
        }
        int count =0;

        for (int i = 0; i<nums.size(); i++)
        {
            if (nums[i] == val)
            {
                count++;
            }
        }

        int k = nums.size()- count;
        

        if (count)
        {
                for (int i = 0; i<=k; i++)
            {

                if (nums[i] == val)
                {
                    
                    int j = i;
                    int to_swap=0;
                    while((nums[j]==val) && (j<int(nums.size())-1))
                    {
                        to_swap=nums[j+1];
                        j++;
                    }
                    nums[i] = to_swap;
                    if (j>=nums.size())
                    {
                        nums[j-1] = val;
                    }
                    else
                    {
                        nums[j] = val;
                    }
                
        
                }
            }
            return k;
            
        }
        else
        {
            return (nums.size());
        }
         

        



    }
};
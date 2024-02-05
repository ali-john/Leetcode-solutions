#include<cmath>
#include<algorithm>
class Solution {
public:
    int majorityElement(vector<int>& nums) 
    {

        int threshold = 0;
        if (nums.size()%2 == 0)
        {
            threshold = nums.size()/2;
        }
        else
        {
            threshold = (nums.size()/2)+1;
        }
        int output=nums[0];
        int count=0;
        sort(nums.begin(),nums.end());
        int offset = 0;
        

        for (int i=1;i<nums.size();i++)
        {
            if (i==nums.size()-1)
            {
                if (nums[i]!=nums[i-1])
                {
                    output = nums[i-1];
                    break;
                }
                else
                {
                    output = nums[i];
                }
                
            }
            if (nums[i]!=nums[i-1])
            {
                count=(i-offset);
                offset = i;
            }
            if (count>=threshold)
            {
                output = nums[i-1];
                break;
            }

            

        }
        return output;


        
    }
};
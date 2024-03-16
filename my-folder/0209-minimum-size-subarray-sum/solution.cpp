class Solution {
public:
    int minSubArrayLen(int target, vector<int>& nums) {
        
        if (nums.size()==1)
        {
            if (target<nums[0])
            {
                return 1;
            }
            else
            {
                return 0;
            }
        }

        if (nums[0]>target)
        {
            return 1;
        }
        //sort(nums.begin(),nums.end());
        int i = 0;
        int  j = 1;
        vector<int> output;
        int sum = accumulate(nums.begin(),nums.end(),0);
        int loop_sum = nums[i]+nums[j];
        if (sum>=target)
        {
            while(j<nums.size())
            {
                

                if (loop_sum<target)
                {
                    j++;
                    if (j<nums.size())
                    {
                        loop_sum +=  (nums[j]); 
                    }
                }
                else
                {
                    output.push_back((j-i)+1);
                    loop_sum = loop_sum -nums[i];
                    i++;
                    
                }

            }
            
            auto min = min_element(output.begin(),output.end());
            return *min;

        }
        else
        {
            return 0;
        }


        
    }
};

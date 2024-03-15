class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        sort(nums.begin(),nums.end());
        int fixed = 0;
        vector<vector<int>> output;
        set<vector<int>> set;
        auto i = nums.begin()+1;
        auto j = nums.end()-1;

        while(fixed<nums.size()-2)
        {
            int first = i - nums.begin();
            int second = j - nums.begin();

            if (first >= second || second<=first)
            {
                fixed++;
                if (nums[fixed]==nums[fixed+1])
                {
                    while(nums[fixed]==nums[fixed+1] && fixed<nums.size()-2)
                    {
                        fixed++;
                    }
                }
                i = nums.begin();
                j = nums.end()-1;

            } 


            int sum = nums[fixed] + *(i) + *(j);
            if (sum<0)
            {
                i++;
                if (i - nums.begin() == fixed)
                {
                    i++;
                }

            }
            else if (sum>0)
            {
                j--;
                if (j - nums.begin() == fixed)
                {
                    j--;
                }
            }
            else
            {
                vector<int> temp;
                if (first != fixed || second !=fixed  || first!=second)
                {
                        temp.push_back(nums[fixed]);
                        temp.push_back(*(i));
                        temp.push_back(*(j));
                        sort(temp.begin(),temp.end());

                    // push only if it not there before
                    set.insert(temp);
                    // update pointers
                    i++;
                    if (i - nums.begin() == fixed)
                    {
                        i++;
                    }
                    
                }

                
            }
            
            
        }

        for (auto it: set)
        {
            output.push_back(it);
        }
        
        return output;
    }
};

class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> prefix_product = nums;
        vector<int> postfix_product = nums;
        vector<int> answer=nums;

        for (int i =1,j=nums.size()-2; i<nums.size(),j>=0;i++,j--)
        {
            int product_pre = prefix_product[i-1] * nums[i];
            prefix_product[i] = product_pre; 
            int product_post  = postfix_product[j+1] * nums[j];
            postfix_product[j] = product_post;
        }
        for (int i=0; i<nums.size();i++)
        {
            if (i==0)
            {
                answer[i] = postfix_product[i+1];
            }
            else if (i==(nums.size()-1))
            {
                
                answer[i] = prefix_product[i-1];
            }
            else
            {

                int p = prefix_product[i-1] * postfix_product[i+1];
                answer[i] = p;
            }
        }
        

        return answer;

    }
};
class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        vector<int> original(nums.begin(),nums.end());
        int n = nums.size();
        for (int i=0; i<n;i++)
        {
            int index = ((i+k)% n);
            nums[index] = original[i]; 

        }
        
    }
};
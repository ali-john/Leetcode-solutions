class Solution {
public:
    long long countSubarrays(vector<int>& nums, int k) {
        int n = nums.size();
        int max = *max_element(nums.begin(), nums.end());
        int count = 0;
        long long ans = 0;


        int left = 0;
        int right = 0;

        while (right < n){
            if (nums[right] == max){
                count+=1;
            }
            while (left <= right && count>=k){
                ans+=1;
                int right_count = n - right - 1;
                ans+=right_count;
                if (nums[left] == max){
                    count-=1;
                }
                left+=1;
            } 
            right+=1;
        }
        return ans;
    }
};

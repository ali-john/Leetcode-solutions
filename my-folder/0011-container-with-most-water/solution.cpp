class Solution {
public:
    int maxArea(vector<int>& height) {
        int left =0;
        int right = height.size()-1;
        int output = 0;

        while (left<right)
        {
            int min_height = min(height[left], height[right]);
            int diff = abs(right - left);
            output = max(output, (min_height)*diff);

            if (height[left]<=height[right])
            {
                left++;
            }
            else
            {
                right--;
            }
            
        }
        return output;
        
    }
};

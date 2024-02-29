class Solution {
public:
    int trap(vector<int>& height) {
        
        int left =0;
        int leftmax = height[0];
        int water_b = 0;
        int total_water = 0;
        int right = 0;
        int right_max = height[height.size()-1];

        for (int i=0; i<height.size();i++)
        {
            if (height[i]>leftmax)
            {
                leftmax = height[i];
                left = i;
            }
            else
            {
                total_water+= leftmax - height[i];
            }
        }
        if (left!=height.size()-1)
        {
            for (int i=height.size()-1; i>left;i--)
            {
                total_water-= (leftmax-height[i]);
                if (height[i]>right_max)
                {
                    right_max = height[i];
                    right = i;
                }
                else
                {
                    total_water+= right_max - height[i];
                }
            }
        }
        return total_water;
    }
};
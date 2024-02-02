class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        vector<int> num3;

        for (int i = 0; i < m; i++) {
            num3.push_back(nums1[i]);
        }
        for (auto i= nums2.begin(); i<nums2.end(); i++)
        {
            num3.push_back(*i);
        }
        for (int i=0; i<m+n; i++)
        {
            for (int j =i+1; j<m+n; j++)
            {
                if (num3[j]< num3[i])
                {
                    swap(num3[i],num3[j]);
                } 
            }
        }

        for (int i=0; i<m+n; i++)
        {
            nums1[i] = num3[i];
        }


    }
};

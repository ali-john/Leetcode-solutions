class Solution {
public:
    int hIndex(vector<int>& citations) {

        
        int h_index = 0;
        int count = 0;
        int temp_h = 0;
        for (int i=0; i<=citations.size();i++)
        {
            temp_h = i;
            count = 0;
            for (int j=0; j<citations.size();j++)
            {
                if (citations[j]>=i)
                {
                    count++;
                }
                if (count>=i)
                {
                    temp_h = i;
                    h_index = max(h_index,temp_h);
                }
            }
        }
        return h_index;
    }
};

class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {

        vector<int> output;
        auto j = numbers.end()-1;
        auto i = numbers.begin();

        int sum = *(i)+ *(j);

        while (sum!=target)
        {
            if (sum<target)
            {
                i++;   
            }
            else
            {
                j--;
            }
            sum = *(i)+ *(j);
        }

        int start_ind = (i - numbers.begin()) +1;
        int end_ind = (j - numbers.begin()) +1;

        output.push_back(start_ind);
        output.push_back(end_ind);
        return output;
        
    }
};

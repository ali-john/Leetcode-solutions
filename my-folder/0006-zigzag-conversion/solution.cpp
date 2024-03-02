#include<vector>
#include<string>
class Solution {
public:
    string convert(string s, int numRows) {

        if (numRows == 1)
        {
            return s;
        }
        else if (numRows>=s.size())
        {
            return s;
        }
        else
        {
            vector<vector<char>> vec(numRows);

            int last_row = 0;
            bool hit_last = false;
            for (int i = 0; i<s.size(); i++)
            {
                char a = s[i];
                vec[last_row].push_back(a);
                if (last_row == numRows -1)
                {
                    hit_last = true;
                }
                else if (last_row == 0)
                {
                    hit_last = false;
                }
                if (hit_last)
                {
                    last_row--;
                }
                else
                {
                    last_row++;
                }
                
            }

                //string output(vec[0].begin(), vec[0].end());
            string output;
            for (int i=0; i<numRows; i++)
            {
                output.insert(output.end(),vec[i].begin(), vec[i].end());
            }
            //string output(output.end(),vec[i].begin(), vec[i].end());

            return output;
        }
        
        

        
        
        
    }
};

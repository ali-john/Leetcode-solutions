class Solution {
public:

    string longestCommonPrefix(vector<string>& strs) 
    {
        string ans="";
        for (int i=0; i<strs[0].size();i++)
        {
            char f = strs[0][i];
            bool match = true;

            for (int j=1; j<strs.size(); j++)
            {   
                if (strs[j][i] != f)
                {
                    match = false;
                }
            }
            if (match)
            {
                ans+=f;
            }
            else
            {
                return ans;
            }
        }
        return ans;
    }
};

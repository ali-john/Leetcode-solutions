class Solution {
public:
    bool isSubsequence(string s, string t) {
        int last_index = 0;
        int found = 0;
        bool decision = false;
        for (int i=0;i<s.size();i++)
        {
            bool in_loop=false;
            for (int j=last_index;j<t.size();j++)
            {
                if (t[j] == s[i])
                {
                    last_index = j+1;
                    found++;
                    in_loop=true;
                    break;
                }
            }
            if(!in_loop)
            {
                break;

            }

        }
        if (found>=s.size())
        {
            decision=true;
        }
        return decision;
        
    }
};

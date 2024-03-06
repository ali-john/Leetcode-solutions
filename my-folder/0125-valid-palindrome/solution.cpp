#include<cstring>
class Solution {
public:
    bool isPalindrome(string s) {
        string forward = "";
        string backward = "";
        for (int i=0; i<s.size();i++)
        {
            if (isalnum(s[i]))
            {
                s[i] = tolower(s[i]);
                forward+=s[i];
            }
        }
        for (int i=forward.size()-1; i>=0;i--)
        {
            backward+=forward[i];
        }
        if (backward==forward)
        {
            return true;
        }
        else
        {
            return false;
        }

    }
};

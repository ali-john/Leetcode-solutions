class Solution {
public:
    int strStr(string haystack, string needle) {

        if (needle.size()>haystack.size())
        {
            return -1;
        }
        char first = needle[0];
        int loc = 0;
        bool match = true;
        for (int i=0; i<haystack.size(); i++)
        {
            if (haystack[i] == first)
            {
                loc = i;
                match = true;
                
                for (int k=loc,j=0; i<haystack.size();k++,j++)
                {
                    if (j<needle.size())
                    {
                        if (haystack[k]!=needle[j])
                        {
                            match = false;
                            break;
                        }
                    }
                    else
                    {
                        break;
                    }
                }
                if (match)
                {
                    return loc;
                }
                
            }

        }

        if (match)
        {
            if (needle[0] == haystack[0])
            {
                return loc;
            }
            else
            {
                return -1;
            }
        }
        else
        {
            return -1;
        }
        
        
    }
};
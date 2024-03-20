class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        set<char> sub;
        int start = 0;
        int max_l = 0;

        for (int end=0;end<s.size();end++)
        {
            char a = s[end];

            auto itr = sub.find(a);
            if (itr!=sub.end())
            {
                
                while(s[start]!=a)
                {
                    sub.erase(s[start]);
                    start++;
                }
                sub.erase(s[start]);
                start++;
                
            }
            sub.insert(a);
            max_l = max(max_l, end-start+1);
        }
        return max_l;
    }
};

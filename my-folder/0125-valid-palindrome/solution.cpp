class Solution {
public:
    bool isPalindrome(string s) {
        string filtered_str, reversed_str;
        
        for (auto ch:s){
            if (isalnum(ch)) filtered_str+=tolower(ch);
        }

        reversed_str.resize(filtered_str.size());
        reverse_copy(filtered_str.begin(), filtered_str.end(), reversed_str.begin());
        return reversed_str == filtered_str;
    }
};

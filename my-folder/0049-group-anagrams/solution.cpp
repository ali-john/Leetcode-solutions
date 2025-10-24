class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> table;
        for (auto str: strs){
            string str_new = str;
            sort(str_new.begin(), str_new.end());
            table[str_new].push_back(str);
        }
        vector<vector<string>> output;
        for (auto& [key,value]: table){
            output.push_back(value);
        }
        return output;
        
    }
};

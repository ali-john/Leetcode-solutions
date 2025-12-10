class Solution {
public:
    bool isAnagram(string s, string t) {
        unordered_map<char, int> table1;
        unordered_map<char, int> table2;

        for (auto ch:s){
            table1[ch]+=1;
        }

        for (auto ch:t){
            table2[ch]+=1;
        }

        for (auto pair: table1){
            char key = pair.first;
            int val = pair.second;

            if (table2.find(key) != table2.end()){
                if (table2[key]!=val)
                    return false;
            } 
            else{
                return false;
            }
        }

        for (auto pair: table2){
            char key = pair.first;
            int val = pair.second;

            if (table1.find(key) != table1.end()){
                if (table1[key]!=val)
                    return false;
            } 
            else{
                return false;
            }
        }
        return true;
        
    }
};

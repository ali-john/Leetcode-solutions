class Solution {
public:
    bool rotateString(string s, string goal) {
        unordered_map<char,int> table;
        unordered_map<char,int> goal_table;
        if (s.size()!=goal.size()) return false;
        for (char chr:s){
            table[chr]+=1;
        }
        for (char chr:goal)
        {
            goal_table[chr]+=1;
        }
        if (table!=goal_table) return false;
       
        string new_string = s + s;
        return new_string.find(goal) < new_string.length();
    }
};

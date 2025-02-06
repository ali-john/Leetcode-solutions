class Solution {
public:
    int maxEqualRowsAfterFlips(vector<vector<int>>& matrix) {
        unordered_map<string,int> table;

        for (auto& row:matrix)
        {
            string pattern = "";
            for (int col = 0; col<row.size(); col++)
            {
                if (row[0] == row[col]){
                    pattern+="T";
                }
                else
                {
                    pattern+="F";
                }
            }
            table[pattern]+=1;
        }

        int ans = 0;
        for (auto& entry:table)
        {
            ans = max(ans,entry.second);
        }
        return ans;
    }
};

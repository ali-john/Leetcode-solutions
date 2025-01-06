class Solution {
public:
    int findJudge(int n, vector<vector<int>>& trust) {
        

        vector<int> in_degree(n,0);
        vector<int> out_degree(n,0);

        for (auto &edge:trust)
        {
            int first = edge[0];
            int second = edge[1];
            in_degree[second-1]+=1;
            out_degree[first-1]+=1;
        }

        for (int i=0; i<n; i++)
        {
            if (in_degree[i] ==n-1 and out_degree[i]==0)
            {
                return i+1;
            }

        }
        return -1;


    }
};

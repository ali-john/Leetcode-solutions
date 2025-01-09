class Solution {
public:
    
    bool dfs(int node,vector<vector<int>>& graph, vector<int>& state)
    {
        if (state[node] != 0) {
            return state[node] == 2;
        }

        state[node] = 1;

        for (int nei : graph[node]) {
            if (state[nei] == 1 || !dfs(nei, graph, state)) {
                return false;
            }
        }

        state[node] = 2;
        return true;
    }
    
    vector<int> eventualSafeNodes(vector<vector<int>>& graph) {
        int n = graph.size();
        
        vector<int> output;
        vector<int> states(n,0); 
        for (int i=0; i<n;i++)
        {
            if ( dfs(i,graph,states) )
                output.push_back(i);
        }

        return output;
    }
};

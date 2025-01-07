class Solution {
public:
    bool isBipartite(vector<vector<int>>& graph) {
        int n = graph.size();
        vector<int> color(n,-1);
        queue<int> q;
        
        for (int node = 0; node<n; node++)
        {
            if ( color[node] == -1) 
            {
                color[node] = 0;
                q.push(node);
                while (!q.empty())
                {
                    int curr = q.front();
                    q.pop();
                    for (auto nei:graph[curr] )
                    {
                        if ( color[nei]==-1 )
                        {
                            color[nei] = 1 - color[curr];
                            q.push(nei);
                        }
                        else if ( color[nei] == color[curr] )
                        {
                            return false;
                        }

                    }
                }

            }
        }
        return true;
    }
};

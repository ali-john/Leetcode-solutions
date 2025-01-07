class Solution {
public:
    int makeConnected(int n, vector<vector<int>>& connections) {
        int edges = connections.size();
        if ( edges < n-1)
            return -1;
        
        unordered_map<int, vector<int>> graph;

        for (int i=0; i<connections.size(); i++)
        {
            graph[connections[i][0]].push_back(connections[i][1]);
            graph[connections[i][1]].push_back(connections[i][0]);
        }
        
        vector<bool> visited(n,false);
        
        int components = 0;
        for (int node = 0; node< n; node++)
        {
            if (!visited[node])
            {
                components+=1;
                queue<int> q;
                q.push(node);
                while (!q.empty())
                {
                    int curr = q.front();
                    q.pop();
                    if (visited[curr]) continue;
                    visited[curr] = true;
                    for (int nei: graph[curr])
                    {
                        if (!visited[nei])
                        {
                            q.push(nei);
                        }
                    }
                }
            }
        }
        
        return components -1;
        
    }
};

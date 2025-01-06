class Solution {
public:
    unordered_map<string,vector<pair<string, double >>> graph;

    double dfs(string first,string end,double path,set<string>& visited)
    {
        if (first==end)
        {
            return path;
        }

        visited.insert(first);
        for (auto &nei: graph[first])
        {
            const string& second = nei.first;
            double weight = nei.second;
            if ( visited.find(second)== visited.end() )
            {
                double val = dfs(second,end,path*weight,visited);
                if (val!=-1)
                {
                    return val;
                }
            }
        }
        return -1.0;
    }


    vector<double> calcEquation(vector<vector<string>>& equations, vector<double>& values, vector<vector<string>>& queries) {
        
        int n = equations.size();
        int m = queries.size();

        for (int i =0; i<n; i++)
        {
            graph[equations[i][0]].push_back({equations[i][1],values[i]});
            graph[equations[i][1]].push_back({equations[i][0],1/values[i]});
        }

        vector<double> output(m);

        for (int i = 0; i<m; i++)
        {
            string first = queries[i][0];
            string second = queries[i][1];

            // If either node is not in the graph, the result is -1.0
            if (graph.find(first) == graph.end() || graph.find(second) == graph.end())
            {
                output[i] = -1.0;
            }
            else if (first == second)
            {
                output[i] = 1.0; // Self-equality case
            }
            else
            {
                set<string> visited;
                double out = dfs(first, second, 1.0, visited);
                output[i] = out;
            }
            
        }
        return output;


        
    }
};

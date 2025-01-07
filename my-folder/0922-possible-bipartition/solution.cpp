class UnionFind{
    public:

        vector<int> root;
        vector<int> rank;
        UnionFind(int n)
        {
            root.resize(n);
            rank.resize(n,1);
            for (int i = 0; i<n; i ++)
            {
                root[i] = i;
            }

        }

        int find(int u)
        {
            if ( root[u] == u)
            {
                return u;
            }
            return root[u] = find(root[u]);
            
        }
        
        void Union(int u, int v)
        {
            int u_parent = find(u);
            int v_parent =find(v);

            if (u_parent!=v_parent)
            {
                if ( rank[u_parent] > rank[v_parent] )
                    root[v_parent] = u_parent;
                else if ( rank[v_parent] > rank[u_parent])
                    root[u_parent] = v_parent;
                else
                {
                    root[u_parent] = v_parent;
                    rank[v_parent]+=1;
                }
            }       
        }

        bool is_connected(int u, int v)
        {
            return find(u) == find(v);
        }
};



class Solution {
public:
    bool possibleBipartition(int n, vector<vector<int>>& dislikes) {
        UnionFind uf(n+1);

        unordered_map<int, vector<int> > graph;

        for (int i =0; i<dislikes.size(); i++)
        {
            graph[dislikes[i][0]].push_back(dislikes[i][1]);
            graph[dislikes[i][1]].push_back(dislikes[i][0]);
        }

        for (int node =1; node<n; node++)
        {
            for (int nei: graph[node] )
            {
                if ( uf.find(nei) == uf.find(node) ) return false;
                uf.Union(graph[node][0],nei);
            }

        }
        return true;

    }
};

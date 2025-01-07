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
    int findCircleNum(vector<vector<int>>& isConnected) {
        int n = isConnected.size();
        UnionFind uf(n+1);
        for (int i = 0; i<isConnected.size();i++)
        {
            for (int j = 0; j<n;j++)
            {
                if (i==j) continue;
                if ( isConnected[i][j]==1 )
                {
                    uf.Union(i+1,j+1);
                }
            }
        }
        int provinces = 0;
        for (int i=1; i<uf.root.size();i++)
        {
            if (uf.root[i]==i)
                provinces+=1;
        }
        return provinces;
    }
};

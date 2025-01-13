class Solution {
public:
    int maxDistance(vector<vector<int>>& grid) {
        int n = grid.size();
        int max_val = INT_MIN;
        queue<tuple<int,int,int>> q;
        set<tuple<int,int>> visited;
        for (int i=0; i<n;i++)
        {
            for (int j=0; j<n;j++)
            {
                if (grid[i][j]==1)
                {
                    q.push(make_tuple(i,j,0));
                    visited.insert(make_tuple(i,j));
                }
            }
        }

        if (q.empty() || q.size()==(n*n))
            return -1;

        vector<vector<int>>directions = {{1,0},{-1,0},{0,1},{0,-1}};
        while (!q.empty())
        {
            auto [x,y,dist] = q.front();
            q.pop();
            max_val = max(max_val,dist);
            
            for (auto dir: directions)
            {
                int new_x = x + dir[0];
                int new_y = y + dir[1];
                if (new_x>=0 && new_x<n && new_y>=0 && new_y<n)
                {
                    if (visited.find(make_tuple(new_x,new_y)) == visited.end() )
                    {
                        q.push(make_tuple(new_x,new_y,dist+1));
                        visited.insert(make_tuple(new_x,new_y));
                    }
                }
            }

        }
        return max_val;
        
    }
};

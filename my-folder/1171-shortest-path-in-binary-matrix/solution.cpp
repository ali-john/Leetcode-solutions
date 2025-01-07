class Solution {
public:
    int shortestPathBinaryMatrix(vector<vector<int>>& grid) {
        
        int n = grid.size();
        if (grid[0][0]==1)
            return -1;
        queue<tuple<int,int,int>> q;
        q.push(make_tuple(1,0,0));

        vector<pair<int,int>> directions = {{1,0}, {0,1}, {-1,0}, {0,-1}, {1,1}, {-1,-1}, {1,-1}, {-1,1}};
        set<pair<int,int>> visited;
        visited.insert({0,0});
        while (!q.empty())
        {
            auto [val,i,j] =  q.front();
            q.pop();
            if (i==n-1 and j==n-1)
                return val;
            
            for (auto direction: directions)
            {
                int new_x = i + direction.first;
                int new_y = j + direction.second;
                if  ( new_x>=0 and new_x < n and new_y>=0 and new_y< n and grid[new_x][new_y] == 0 )
                {
                    if ( visited.find({new_x,new_y}) == visited.end() )
                    {
                        q.push(make_tuple(val+1,new_x,new_y));
                        visited.insert({new_x,new_y});
                    }
                }
            }
        }
        return -1;



    }
};

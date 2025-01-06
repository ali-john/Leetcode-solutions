class Solution {
public:

    int orangesRotting(vector<vector<int>>& grid) {
        
        int rows = grid.size();
        int cols = grid[0].size();
        queue<pair<int,int>> q;
        vector<vector<int>> directions = {{0,1},{0,-1},{1,0},{-1,0}};

        for (int i =0; i<rows;i++)
        {
            for (int j = 0; j<cols;j++)
            {
                if (grid[i][j] == 2)
                {
                    q.push({i,j});
                }
            }
        }

        int time = 0;

        while (!q.empty())
        {
            int length = q.size();
            time+=1;

            while (length--)
            {
                auto curr = q.front();
                q.pop();
                int x = curr.first;
                int y = curr.second;

                for (auto direction: directions)
                {
                    int new_x = x + direction[0];
                    int new_y = y + direction[1];

                    if ( new_x>= 0 && new_x < rows && new_y>=0 && new_y < cols && grid[new_x][new_y] ==1 )
                    {
                        grid[new_x][new_y] = 2;
                        q.push({new_x,new_y});
                    }
                }

            }
                
        }

        for (int i =0; i<rows; i++)
        {
            for (int j =0; j<cols; j++)
            {
                if (grid[i][j]==1)
                {
                    return -1;
                }
            }
        }
        return max(0,time-1);




        

    }
};

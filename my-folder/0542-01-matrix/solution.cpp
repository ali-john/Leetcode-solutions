class Solution {
public:
    vector<vector<int>> updateMatrix(vector<vector<int>>& mat) {
        int rows = mat.size();
        int cols = mat[0].size();
        queue<pair<int,int>> q;
        vector<vector<int>> result(rows, vector<int>(cols,-1));
        vector<vector<int>> directions = {{0,1},{0,-1}, {1,0}, {-1,0}};

        for (int i =0; i<rows; i++)
        {
            for (int j =0; j<cols; j++)
            {
                if ( mat[i][j] == 0)
                {
                    result[i][j] = 0;
                    q.push({i,j});
                }
                    
            }
        }

        while (!q.empty())
        {
            pair<int, int> p = q.front();
            q.pop();

            for (auto direction: directions)
            {
                int new_x = p.first + direction[0];
                int new_y = p.second + direction[1];
                if (new_x>=0 && new_x<rows && new_y>=0 && new_y<cols and result[new_x][new_y]==-1)
                {
                    result[new_x][new_y] = result[p.first][p.second] + 1;
                    q.push({new_x,new_y});
                }
            }
        }
        return result;
    }
};

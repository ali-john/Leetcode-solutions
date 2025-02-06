class Solution {
public:
    int countUnguarded(int m, int n, vector<vector<int>>& guards, vector<vector<int>>& walls) {
        
        // Gaurd = 2
        // empty = -1
        // wall = 3
        vector<vector<int>> matrix(m, vector<int>(n,-1));

        for (auto& g:guards) matrix[g[0]][g[1]] = 2;
        for (auto& w:walls) matrix[w[0]][w[1]] = 3;
        
        vector<vector<int>> directions = {{1,0}, {-1,0}, {0,1}, {0,-1}}; 

        for (auto& guard:guards)
        {
            // go in each direction as far as possible
            int x = guard[0];
            int y = guard[1];  
            for (auto& dir: directions)
            {
                int new_x = x + dir[0];
                int new_y = y + dir[1];
                while (new_x>=0 && new_x<m && new_y>=0 && new_y<n && matrix[new_x][new_y]!=3 && matrix[new_x][new_y]!=2)
                {
                    matrix[new_x][new_y] = 0;
                    new_x = new_x + dir[0];
                    new_y = new_y + dir[1];
                }
            }
        }

        int ans = 0;
        for (int i= 0; i<m; i++)
        {
            for (int j=0; j<n; j++)
            {
                if (matrix[i][j] == -1) ans+=1;
            }
        }
         return ans;



    }
};

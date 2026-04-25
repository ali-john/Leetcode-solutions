class Solution {
public:
    int modulo = 1e9 + 7;
    int f(vector<vector<int>>& grid, int i, int j, int zor, int k, vector<vector<vector<int>>>& dp)
    {
        if (i < 0 || j<0)
            return 0;
        if (i == 0 && j == 0)
            if ((zor ^ grid[i][j]) == k)
                return 1;
            else
                return 0;
            
        if (dp[i][j][zor] != -1)
            return dp[i][j][zor];

        int xornow = ((zor)^(grid[i][j]));
        int top = f(grid, i - 1, j, xornow, k, dp);
        int right = f(grid, i, j - 1, xornow, k, dp);
        return dp[i][j][zor] = (top + right) % modulo;
 
    }   

    int countPathsWithXorValue(vector<vector<int>>& grid, int k) {
        int m = grid.size();
        int n = grid[0].size();
        vector<vector<vector<int>>> dp(m, vector<vector<int>>(n, vector<int>(16,-1)));
        return f(grid, m - 1, n - 1, 0, k, dp);
    }
};

class Solution {
public:

    void dfs(int i,int j,int rows,int cols,vector<vector<int>>& grid)
    {
        if (i>=0 && i<rows && j>=0 && j<cols and grid[i][j]==1)
        {
            grid[i][j] = 'T';
            dfs(i+1,j,rows,cols,grid);
            dfs(i-1,j,rows,cols,grid);
            dfs(i,j+1,rows,cols,grid);
            dfs(i,j-1,rows,cols,grid);
        }
        else
        {
            return;
        }
            
    }
    int numEnclaves(vector<vector<int>>& grid) {
        int rows = grid.size();
        int cols = grid[0].size();

        // set all boundary lands and connected land to 't'
        for (int i=0; i<rows;i++)
        {
            for (int j=0; j<cols;j++)
            {
                if (i==0 or i==rows-1 or j==0 or j==cols-1)
                {
                    dfs(i,j,rows,cols,grid);
                }
            }
        }

        // the remaining 1s are the region that can not be walked off
        int count = 0;
        for (int i=0; i<rows;i++)
        {
            for (int j=0; j<cols;j++)
            {
                if ( grid[i][j] ==1)
                    count+=1;   
            }
        }
        return count;

    }
};

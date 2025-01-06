class Solution {
public:
    void dfs(int r, int c, vector<vector<char>>& board)
        {
            int rows = board.size();
            int cols = board[0].size();
            if  ( (r< 0 or r>=rows) or (c<0 or c>=cols) or (board[r][c]!='O') ) return;
            board[r][c] = 'T';
            dfs(r+1,c, board);
            dfs(r-1,c,board);
            dfs(r,c+1,board);
            dfs(r,c-1,board);
        }

    void solve(vector<vector<char>>& board) {
        
        int rows = board.size();
        int cols = board[0].size();
        
        
        for (int i = 0; i<rows;i++)
        {
            for (int j = 0; j<cols; j++)
            {
                if ( (i==0 or i ==rows -1 or j==0 or j==cols -1 ) and (board[i][j]=='O') )
                {
                    dfs(i,j,board);
                }
            }
        }

        for (int i= 0; i< rows; i++)
        {
            for (int j = 0; j<cols;j++)
            {
                if (board[i][j]== 'O')
                {
                    board[i][j] = 'X';
                }
            }
        }

        for (int i= 0; i< rows; i++)
        {
            for (int j = 0; j<cols;j++)
            {
                if (board[i][j]== 'T')
                {
                    board[i][j] = 'O';
                }
            }
        }
        
    }
};

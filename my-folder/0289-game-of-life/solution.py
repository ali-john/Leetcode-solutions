class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row = len(board)  # 4
        col = len(board[0])  # 3
        changes = []

        for i in range(row):
            for j in range(col):
                val = board[i][j]
                top_left = board[i-1][j-1] if (i-1) >= 0 and (j-1) >= 0 else 0
                top = board[i-1][j] if (i-1) >= 0 else 0
                top_right = board[i-1][j+1] if (i-1) >= 0 and (j+1) < col else 0
                right = board[i][j+1] if (j+1) < col else 0
                left = board[i][j-1] if (j-1) >= 0 else 0
                bottom_left = board[i+1][j-1] if (i+1) < row and (j-1) >= 0 else 0
                bottom = board[i+1][j] if (i+1) < row else 0
                bottom_right = board[i+1][j+1] if (i+1) < row and (j+1) < col else 0
                total = sum([
                    top_left,
                    top,
                    top_right,
                    right,
                    left,
                    bottom_left,
                    bottom,
                    bottom_right
                ])
                if val == 1:
                    if total < 2:
                        changes.append(((i, j), 0))
                    elif total == 2 or total == 3:
                        continue
                    elif total > 3:
                        changes.append(((i, j), 0))
                elif val == 0:
                    if total == 3:
                        changes.append(((i, j), 1))

        for ((i, j), val) in changes:
            board[i][j] = val
                    

                









        

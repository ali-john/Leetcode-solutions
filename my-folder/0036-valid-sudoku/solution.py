class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        col_data = []
        row_data = []
        row_digit = False
        col_digit = False
        for i in range(9): # row checking
            for j in range(9):
                if board[i][j].isdigit() is True:
                    row_data.append(board[i][j])
                    row_digit = True
                else:
                    continue
            if len(row_data)>0 and len(row_data) == len(set(row_data)):
                row_data.clear()
                row_digit = False
                continue
            else:
                if row_digit is True:
                    return False
                else:
                    row_digit = False
                row_digit = False
                row_data.clear()

        for i in range(9): # col checking
            for j in range(9):
                if board[j][i].isdigit():
                    col_data.append(board[j][i])
                    col_digit = True
                else:
                    continue
            if len(col_data)>0 and len(col_data) == len(set(col_data)):
                col_data.clear()
                col_digit = False
                continue
            else:
                if col_digit:
                    return False
                else:
                    col_digit = False
                col_data.clear()
        grid = []
        grid_data = []
        grid_digit = False
        for i in range(0,9,3):
            for j in range(0,9,3):
                grid.append(board[i][j:j+3])
                grid.append(board[i+1][j:j+3])
                grid.append(board[i+2][j:j+3])
                for x in range(3):
                    for y in range(3):
                        if grid[x][y].isdigit() is True:
                            grid_digit = True
                            grid_data.append(grid[x][y])
                if len(grid_data)>0 and len(grid_data)==len(set(grid_data)):
                    grid_data.clear()
                    grid.clear()
                    grid_digit = False
                    continue
                else:
                    if grid_digit is True:
                        return False
                    else:
                        grid_digit = False
                    grid_data.clear()
                    grid.clear()
        
        return True



            


        

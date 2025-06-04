class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        valid = True

        # check rows

        for row in board:

            seen = set()
            for ele in row:
                if ele!='.' and ele in seen:
                    valid = False
                    return valid
                seen.add(ele)
        
        for col in range(9):
            seen = set()
            for row in range(9):
                ele = board[row][col]
                if ele!='.' and ele in seen:
                    valid = False
                    return valid
                seen.add(ele)


        for row in range(0,9,3):
            for col in range(0,9,3):
                seen = set()

                for i in range(3):
                    for j in range(3):
                        ele = board[row+i][col+j]
                        if ele!='.' and ele in seen:
                            valid = False
                            return valid
                        seen.add(ele)

        return valid

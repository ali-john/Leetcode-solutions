class Solution:
    def checkTwoChessboards(self, co1: str, co2: str) -> bool:
        # black boxes are odd 
        # white boxes are even
        row1 = co1[0]
        col1 = co1[1]
        row2 = co2[0]
        col2 = co2[1]

        # check for coordinate 1:
        diff_row = ord(row1) - ord('a')
        row1_dec = False
        for i in range(diff_row):
            row1_dec = not row1_dec
        for i in range(int(col1)):
            row1_dec = not row1_dec


        diff_2 = ord(row2) - ord('a')
        row2_dec = False
        for i in range(diff_2):
            row2_dec = not row2_dec
        for i in range(int(col2)):
            row2_dec = not row2_dec

        return row1_dec==row2_dec

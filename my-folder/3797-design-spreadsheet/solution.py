class Spreadsheet:

    def __init__(self, rows: int):
        # represent as 2D vector.
        self.sheet = [[ 0 for j in range(26)] for i in range(rows+1)]

    def setCell(self, cell: str, value: int) -> None:
        column = int( ord(cell[0]) - ord('A') )
        row = int(cell[1:])
        self.sheet[row][column] = value

    def resetCell(self, cell: str) -> None:
        column = int( ord(cell[0]) - ord('A') )
        row = int(cell[1:])
        self.sheet[row][column] = 0
        
    def getValue(self, formula: str) -> int:
        first, second = formula.split("+")[0][1:], formula.split("+")[1]
        f = 0
        s = 0
        if first.isdigit(): f = int(first)
        else:
            column = int( ord(first[0]) - ord('A') )
            row = int(first[1:])
            f = self.sheet[row][column]
        
        if second.isdigit(): s = int(second)
        else:
            column = int( ord(second[0]) - ord('A') )
            row = int(second[1:])
            s = self.sheet[row][column]
        
        return f + s


        


# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)

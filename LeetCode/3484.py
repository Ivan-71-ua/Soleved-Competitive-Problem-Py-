
class Spreadsheet:
    def get_xy(self, cell):
        return (ord(cell[0]) - ord('A'), int(cell[1:]) - 1)
    def __init__(self, rows: int):
        self.table = [rows * [0] for _ in range(26)]

    def setCell(self, cell: str, value: int) -> None:
        col, row = self.get_xy(cell)
        self.table[col][row] = value

    def resetCell(self, cell: str) -> None:
        col, row = self.get_xy(cell)
        self.table[col][row] = 0

    def getValue(self, formula: str) -> int:
        f, s = formula[1:].split("+")
        if s.isdigit() and f.isdigit():
            return int(s) + int(f)
        elif s.isdigit():
            col, row = self.get_xy(f)
            return self.table[col][row] + int(s)
        elif f.isdigit():
            col, row = self.get_xy(s)
            return self.table[col][row] + int(f)
        col1, row1 = self.get_xy(s)
        col2, row2 = self.get_xy(f)
        return self.table[col1][row1] + self.table[col2][row2]




# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)
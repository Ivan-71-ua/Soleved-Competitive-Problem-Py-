
class Spreadsheet:
    def __init__(self, rows: int):
        self.table = {}
    def setCell(self, cell: str, value: int) -> None:
        self.table[cell] = value
    def resetCell(self, cell: str) -> None:
        self.table[cell] = 0
    def getValue(self, formula: str) -> int:
        f, s = formula[1:].split('+')
        num1, num2 = 0, 0
        if f in self.table:
            num1 = self.table[f]
        else:
            if f.isdigit():
                num1 = int(f)

        if s in self.table:
            num2 = self.table[s]
        else:
            if s.isdigit():
                num2 = int(s)
        return num1 + num2
# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)
class TicTacToe:

    def __init__(self, n: int):
        self.rows = [0] * n
        self.cols = [0] * n
        self.diag1 = 0
        self.diag2 = 0
        self.n = n

    def move(self, row: int, col: int, player: int) -> int:
        code = -1 if player == 2 else 1

        self.rows[row] += code
        self.cols[col] += code
        if row == col:
            self.diag1 += code
        if (row + col) == (self.n - 1):
            self.diag2 += code

        if (abs(self.rows[row]) == self.n or abs(self.cols[col]) == self.n or abs(self.diag1) == self.n or
            abs(self.diag2) == self.n):
            return player
        return 0
        
        


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
from random import sample

settings = {
    "Простой": (8, 8, 10),
    "Средний": (16, 16, 40),
    "Сложный": (30, 16, 99),
    "Эксперт": (30, 20, 200),
}


class MineField:
    def __init__(
        self, cols: int, rows: int, mines: int, start_point: tuple[int, int]
    ) -> None:
        self.cols, self.rows = cols, rows
        self.field = [["" for _ in range(cols)] for _ in range(rows)]
        it_field = [
            i for i in range(cols * rows) if i != start_point[0] * cols + start_point[1]
        ]
        mine_position = sample(it_field, mines)
        for i in mine_position:
            self.field[i // cols][i % cols] = "x"
        for i in range(rows):
            for j in range(cols):
                if not self.field[i][j]:
                    count_mine = 0
                    for k in range(i - (i != 0), i + (i + 1 < rows) + 1):
                        for m in range(j - (j != 0), j + (j + 1 < cols) + 1):
                            if i != k or m != j:
                                count_mine += self.field[k][m] == "x"
                    self.field[i][j] = f"{count_mine}"
        self.visual_field = [["" for _ in range(cols)] for _ in range(rows)]

    def recur_open(self, i, j):
        for k in range(i - (i != 0), i + (i + 1 < self.rows) + 1):
            for m in range(j - (j != 0), j + (j + 1 < self.cols) + 1):
                if i != k or m != j:
                    if self.field[k][m] == "0" and self.visual_field[k][m] != "0":
                        self.visual_field[k][m] = self.field[k][m]
                        self.open(k, m)
                    else:
                        self.visual_field[k][m] = self.field[k][m]

    def open(self, i, j):
        self.visual_field[i][j] = self.field[i][j]
        if self.visual_field[i][j] == "x":
            return "lose"
        if self.visual_field[i][j] == "0":
            self.recur_open(i, j)
        return self.prov()

    def prov(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if (
                    self.field[i][j] != "X"
                    and self.field[i][j] != self.visual_field[i][j]
                ):
                    return
        return "win"

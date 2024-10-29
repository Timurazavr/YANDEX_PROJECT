from random import sample


class MineField:
    def __init__(
        self, cols: int, rows: int, mines: int, start_point: tuple[int, int]
    ) -> None:
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

    def open(self, x, y):
        self.visual_field[x][y] = self.field[x][y]


# def recur_open(i, j):
#     for k in range(i - (i != 0), i + (i + 1 < row) + 1):
#         for m in range(j - (j != 0), j + (j + 1 < col) + 1):
#             if i != k or m != j:
#                 if field[k][m] == " 0 " and visual_field[k][m] != " 0 ":
#                     visual_field[k][m] = " 0 "
#                     recur_open(k, m)
#                 else:
#                     visual_field[k][m] = field[k][m]


# field = [["" for _ in range(col)] for _ in range(row)]

# mine_position = sample(range(col * row), mine)
# for i in mine_position:
#     field[i // col][i % col] = " X "

# for i in visual_field:
#     print(*i)
# fl = True
# while True:
#     try:
#         a, b, d = map(int, input().split())
#     except Exception:
#         print("Неверный ввод!")
#         continue
#     if not (0 < a <= row and 0 < b <= col and 0 < d < 5):
#         print("Неверный ввод!")
#         continue
#     a -= 1
#     b -= 1
#     if d == 2 and visual_field[a][b] in ("[ ]", "[?]"):
#         visual_field[a][b] = "[F]"
#     elif d == 3 and visual_field[a][b] in ("[ ]", "[F]"):
#         visual_field[a][b] = "[?]"
#     elif d == 4 and visual_field[a][b] in "('[F]', '[?]')":
#         visual_field[a][b] = "[ ]"
#     else:
#         if visual_field[a][b] == "[ ]":
#             if field[a][b] == " X ":
#                 print("Вы проиграли")
#                 for i in field:
#                     print(*i)
#                 break
#             visual_field[a][b] = field[a][b]
#             if field[a][b] == " 0 ":
#                 recur_open(a, b)

#     for i in visual_field:
#         print(*i)

#     for i in range(row):
#         if not fl:
#             break
#         for j in range(col):
#             if field[i][j] != " X " and field[i][j] != visual_field[i][j]:
#                 fl = False
#                 break
#     if fl:
#         print("Победа!")
#         break
#     fl = True

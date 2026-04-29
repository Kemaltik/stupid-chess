class Pawn:
    def __init__(self, colour : str):
        self.colour = colour
        has_moved = False

def initialize_board()->list:
    wa2 = Pawn("white")
    wb2 = Pawn("white")
    wc2 = Pawn("white")
    wd2 = Pawn("white")
    we2 = Pawn("white")
    wf2 = Pawn("white")
    wg2 = Pawn("white")
    wh2 = Pawn("white")

    ba8 = Pawn("black")
    bb8 = Pawn("black")
    bc8 = Pawn("black")
    bd8 = Pawn("black")
    be8 = Pawn("black")
    bf8 = Pawn("black")
    bg8 = Pawn("black")
    bh8 = Pawn("black")

    row_8 =  "x", "x", "x", "x", "x", "x", "x", "x"
    row_7 =  ba8, bb8, bc8, bd8, be8, bf8, bg8, bh8
    row_6 =  "x", "x", "x", "x", "x", "x", "x", "x"
    row_5 =  "x", "x", "x", "x", "x", "x", "x", "x"
    row_4 =  "x", "x", "x", "x", "x", "x", "x", "x"
    row_3 =  "x", "x", "x", "x", "x", "x", "x", "x"
    row_2 =  wa2, wb2, wc2, wd2, we2, wf2, wg2, wh2
    row_1 =  "x", "x", "x", "x", "x", "x", "x", "x"
    chessboard = [row_8, row_7, row_6, row_5, row_4, row_3, row_2, row_1, row_1]
    return chessboard

chessboard = initialize_board()
for row in chessboard:
    for space in row:
        print(space, end=" ")
    print()


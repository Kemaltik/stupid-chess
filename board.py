def search_for_target(board : list, target, object_search = False):
    #gets the row
    position_x = 0
    position_y = 0
    for row in board:
        if object_search:
            for obj in row:
                if hasattr(obj, "name") and obj.name in target:
                    return position_x, position_y
                else: position_x = position_x + 1
        else:
            if target in row:
                for position in row:
                    if position == target:
                        return position_x, position_y
                    else:
                        position_x = position_x + 1
        position_y = position_y + 1
        position_x = 0
    return "Search Failed"

def search_for_occupation(board : list, position_x : int, position_y : int):
    if board[position_y][position_x] == "x":
        return "x"
    else:
        return board[position_y][position_x].name

class Pawn:
    def __init__(self, colour : str, name : str):
        self.colour = colour
        self.name = name
        self.has_moved = False
        self.piece_type = "pawn"
        self.occupation = "piece"


def initialize_board()->list:
    wa2 = Pawn("white", "a2")
    wb2 = Pawn("white", "b2")
    wc2 = Pawn("white", "c2")
    wd2 = Pawn("white", "d2")
    we2 = Pawn("white", "e2")
    wf2 = Pawn("white", "f2")
    wg2 = Pawn("white", "g2")
    wh2 = Pawn("white", "h2")

    ba8 = Pawn("black", "a8")
    bb8 = Pawn("black", "b8")
    bc8 = Pawn("black", "c8")
    bd8 = Pawn("black", "d8")
    be8 = Pawn("black", "e8")
    bf8 = Pawn("black", "f8")
    bg8 = Pawn("black", "g8")
    bh8 = Pawn("black", "h8")

    row_8 =  "x", "x", "x", "x", "x", "x", "x", "x"
    row_7 =  ba8, bb8, bc8, bd8, be8, bf8, bg8, bh8
    row_6 =  "x", "x", "x", "x", "x", "x", "x", "x"
    row_5 =  "x", "x", "x", "t", "x", "x", "x", "x"
    row_4 =  "x", "x", "x", "x", "x", "x", "x", "x"
    row_3 =  "x", "x", "x", "x", "x", "x", "x", "x"
    row_2 =  wa2, wb2, wc2, wd2, we2, wf2, wg2, wh2
    row_1 =  "x", "x", "x", "x", "x", "x", "x", "x"
    chessboard = [row_8, row_7, row_6, row_5, row_4, row_3, row_2, row_1, row_1]
    return chessboard

chessboard = initialize_board()
print(search_for_occupation(chessboard, 2, 1))


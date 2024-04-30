def getChessSquareColor(column, row):
    if column > 7 or column < 0 or row > 7 or row < 0:
        return ""
    elif column % 2 == row % 2:
        return "white"
    else:
        return "black"


assert getChessSquareColor(0, 0) == 'white'
assert getChessSquareColor(1, 0) == 'black'
assert getChessSquareColor(0, 1) == 'black'
assert getChessSquareColor(7, 7) == 'white'
assert getChessSquareColor(0, 8) == ''
assert getChessSquareColor(2, 9) == ''
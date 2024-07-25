def isEmptyCell(board, col):
    if board[0][col] == 0:
        return True
    return False


def getBestPositionRefined(board, depth):
    best_score = float("-inf")
    global bestPos
    alpha = float("-inf")
    beta = float("inf")
    for col in getPossibleMoves(board):
        row = getUpcomingEmptyRow(board, col)
        board_copy = board.copy()
        board_copy[row][col] = 2
        score = refinedMinimax(board_copy, depth - 1, alpha, beta, False)
        if score > best_score:
            best_score = score
            bestPos = col
        alpha = max(alpha, score)
    return bestPos


def getBestPositionNormal(board, depth):
    best_score = float("-inf")
    global bestPos
    for col in getPossibleMoves(board):
        row = getUpcomingEmptyRow(board, col)
        board_copy = board.copy()
        board_copy[row][col] = 2
        score = normalMinimax(board_copy, depth - 1, False)
        if score > best_score:
            best_score = score
            bestPos = col
    return bestPos


def getUpcomingEmptyRow(board, c):
    for row in reversed(range(6)):
        if board[row][c] == 0:
            return row
    return -1

def normalMinimax(board, depth, maximizingPlayer):
    if depth == 0 or isTerminalState(board):
        if isTerminalState(board):
            if isWinningTurn(board, 1):
                return float("-inf")
            elif isWinningTurn(board, 2):
                return float("inf")
            else:
                return 0
        else:
            return boardEvaluation(board, 2)

    if maximizingPlayer:
        maxEval = float("-inf")
        for col in getPossibleMoves(board):
            row = getUpcomingEmptyRow(board, col)
            board_copy = board.copy()
            board_copy[row][col] = 2
            eval = normalMinimax(board_copy, depth - 1, False)
            maxEval = max(maxEval, eval)
        return maxEval
    else:
        minEval = float("inf")
        for col in getPossibleMoves(board):
            row = getUpcomingEmptyRow(board, col)
            board_copy = board.copy()
            board_copy[row][col] = 1
            eval = normalMinimax(board_copy, depth - 1, True)
            minEval = min(minEval, eval)
        return minEval


def refinedMinimax(board, depth, alpha, beta, maximizingPlayer):
    if depth == 0 or isTerminalState(board):
        if isTerminalState(board):
            if isWinningTurn(board, 1):
                return float("-inf")
            elif isWinningTurn(board, 2):
                return float("inf")
            else:
                return 0
        else:
            return boardEvaluation(board, 2)

    if maximizingPlayer:
        maxEval = float("-inf")
        for col in getPossibleMoves(board):
            row = getUpcomingEmptyRow(board, col)
            board_copy = board.copy()
            board_copy[row][col] = 2
            eval = refinedMinimax(board_copy, depth - 1, alpha, beta, False)
            maxEval = max(maxEval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return maxEval
    else:
        minEval = float("inf")
        for col in getPossibleMoves(board):
            row = getUpcomingEmptyRow(board, col)
            board_copy = board.copy()
            board_copy[row][col] = 1
            eval = refinedMinimax(board_copy, depth - 1, alpha, beta, True)
            minEval = min(minEval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return minEval


def isWinningTurn(board, circle):
    for i in range(3):
        for j in range(3, 4):
            if board[i][j] == circle and board[i + 1][j - 1] == circle and board[i + 2][j - 2] == circle and \
                    board[i + 3][j - 3] == circle:
                return True

    for j in range(4):
        for i in range(6):
            if board[i][j] == circle and board[i][j + 1] == circle and board[i][j + 2] == circle and board[i][
                j + 3] == circle:
                return True

    for j in range(7):
        for i in range(3):
            if board[i][j] == circle and board[i + 1][j] == circle and board[i + 2][j] == circle and board[i + 3][
                j] == circle:
                return True
    for j in range(4):
        for i in range(3):
            if board[i][j] == circle and board[i + 1][j + 1] == circle and board[i + 2][j + 2] == circle and \
                    board[i + 3][j + 3] == circle:
                return True

    return False


def evaluateSum(window, thisPlayerCircle):
    opponentCircle = 3 - thisPlayerCircle
    thisPlayerSum = 0
    opponentSum = 0
    emptySum = 0

    for cell in window:
        if cell == thisPlayerCircle:
            thisPlayerSum += 1
        elif cell == opponentCircle:
            opponentSum += 1
        else:
            emptySum += 1

    nodeSum = 0

    if thisPlayerSum == 3 and emptySum == 1:
        nodeSum += 10
    elif thisPlayerSum == 2 and emptySum == 2:
        nodeSum += 6
    elif thisPlayerSum == 4:
        nodeSum += 1000000
    if opponentSum == 3 and emptySum == 1:
        nodeSum -= 10

    return nodeSum

def boardEvaluation(board, circle):
    sum = 0
    for rows in range(6):
        for cols in range(4):
            winningEdge = []
            for i in range(4):
                winningEdge.append(board[rows][cols + i])
            sum += evaluateSum(winningEdge, circle)
    for cols in range(7):
        for rows in range(3):
            winningEdge = []
            for i in range(4):
                winningEdge.append(board[rows + i][cols])
            sum += evaluateSum(winningEdge, circle)

    for rows in range(3):
        for cols in range(4):
            winningEdge = []
            for i in range(4):
                winningEdge.append(board[rows + i][cols + i])
            sum += evaluateSum(winningEdge, circle)

    for i in range(3):
        for j in range(4):
            winningEdge = []
            for i in range(4):
                winningEdge.append(board[i + 3 - i][j + i])
            sum += evaluateSum(winningEdge, circle)
    return sum


def isTerminalState(board):
    return isWinningTurn(board, 1) or isWinningTurn(board, 2) or len(getPossibleMoves(board)) == 0


def getPossibleMoves(board):
    possibleCellsArray = []
    for c in range(7):
        if isEmptyCell(board, c):
            possibleCellsArray.append(c)
    return possibleCellsArray




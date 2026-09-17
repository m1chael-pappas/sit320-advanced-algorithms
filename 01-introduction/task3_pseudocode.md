# SIT320 - Task 3: Tic-Tac-Toe Playing Algorithm (Pseudocode)

## Strategy

My algorithm uses **minimax**: it explores every possible future game state
recursively, assuming both players play perfectly. The computer (the
*maximising* player) picks the move leading to the best guaranteed outcome; it
assumes the opponent (the *minimising* player) always replies with their best
move.

Because Tic-Tac-Toe has at most 9! ≈ 362,880 game sequences, a full search is
cheap and the computer becomes unbeatable — it will always win or draw.

Scores are depth-adjusted (`10 - depth` for a win, `depth - 10` for a loss) so
the computer prefers *fast* wins and *slow* losses.

## Pseudocode

```
function BEST-MOVE(board, computerPlayer):
    bestScore ← -infinity
    bestMove  ← null
    for each empty cell c in board:
        board[c] ← computerPlayer
        score ← MINIMAX(board, depth = 0, isMaximising = false)
        board[c] ← empty                     // undo the move
        if score > bestScore:
            bestScore ← score
            bestMove  ← c
    return bestMove


function MINIMAX(board, depth, isMaximising):
    if WINNER(board) = computerPlayer:  return 10 - depth   // sooner is better
    if WINNER(board) = humanPlayer:     return depth - 10   // later is better
    if board is full:                   return 0            // draw

    if isMaximising:                         // computer's turn
        best ← -infinity
        for each empty cell c in board:
            board[c] ← computerPlayer
            best ← MAX(best, MINIMAX(board, depth + 1, false))
            board[c] ← empty
        return best
    else:                                    // human's turn
        best ← +infinity
        for each empty cell c in board:
            board[c] ← humanPlayer
            best ← MIN(best, MINIMAX(board, depth + 1, true))
            board[c] ← empty
        return best


function WINNER(board):
    for each line L in {3 rows, 3 columns, 2 diagonals}:
        if all three cells of L hold the same non-empty symbol:
            return that symbol
    return none


// Main game loop (human is X and moves first)
board ← 3x3 grid of empty cells
currentPlayer ← human

while WINNER(board) = none AND board is not full:
    if currentPlayer = human:
        move ← read cell number from user input
        if move is not a valid empty cell:
            print "Invalid move, try again"
            continue                          // re-prompt, don't switch turns
    else:
        move ← BEST-MOVE(board, computerPlayer)
    board[move] ← currentPlayer's symbol
    print board
    currentPlayer ← the other player

if WINNER(board) ≠ none:  print WINNER(board) + " wins!"
else:                     print "It's a draw!"
```

## Complexity

- Time: O(b!) in the branching depth — at most 9! states, trivially fast here.
- Space: O(9) recursion depth (the board is mutated and undone in place).

A working implementation is in `task3_tictactoe.ipynb`.

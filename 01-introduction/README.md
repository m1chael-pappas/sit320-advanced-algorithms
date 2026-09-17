# Introduction

SIT320 task 1.
Getting the toolchain running and writing a first algorithm from scratch.

## Files

| File | Contents |
| --- | --- |
| `task2_basic_script.ipynb` | Counts down from a starting number, classifies each value, and totals the even ones. Written to exercise `while` and `if` in the unit conda environment. |
| `task3_pseudocode.md` | Pseudocode for the tic-tac-toe player, with the reasoning behind depth-adjusted minimax scores. |
| `task3_tictactoe.ipynb` | The same algorithm implemented and playable. The human plays X, the computer plays O and searches the full game tree, so it never loses. |
| `TicTacToe_P12.ipynb` | The lab's starting notebook, downloaded from an external repository and given to us to read, test and repair. Not my code, and its header records where it came from. |

Scoring is `10 - depth` for a win and `depth - 10` for a loss, which makes the computer take the fastest win available and drag out a loss it cannot avoid.

## Running it

```
jupyter notebook task3_tictactoe.ipynb
```

No third-party packages are needed.

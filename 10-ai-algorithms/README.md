# Tic-tac-toe as a Markov Decision Process

SIT320 Advanced Algorithms, distinction task D1.
Michael Pappas.

Tic-tac-toe is reformulated as an MDP and solved exactly with policy iteration and value iteration, then learned from experience with tabular Q-learning against the same environment treated as a black box.
The two approaches are compared on convergence, playing strength and how close the learned Q-table gets to the optimal value function.

The agent plays X and moves first.
The opponent plays O uniformly at random among the empty cells and is folded into the transition model, which gives 3381 states, 2423 of them non-terminal, and 24258 non-zero transitions.

## Results

| Method | Model needed | Time (s) | V(start) | Win vs random | Loss vs minimax |
| --- | --- | --- | --- | --- | --- |
| Policy iteration | yes | 0.16 | 0.7927 | 0.993 | 0.000 |
| Value iteration | yes | 0.17 | 0.7927 | 0.993 | 0.000 |
| Q-learning, 40000 episodes | no | 2.54 | 0.7617 | 0.971 | 0.000 |

The two dynamic programming solvers agree on every state.
Q-learning gets within two percentage points of their win rate without ever reading the transition model, and also never loses to a minimax opponent, but its value estimates stay below V* in the states it visits rarely.

## Files

| File | Contents |
| --- | --- |
| `SIT320_D1_TicTacToe_MDP.ipynb` | Runs everything end to end. Every number and figure in the report comes from this notebook. |
| `TicTacToeMDP.py` | State space, reward function and sparse transition model. Exposes `reset()` and `blackbox_move(s, a)` for the model-free agent. |
| `TicTacToeDP.py` | `TicTacToePolicyIteration` and `TicTacToeValueIteration`, mirroring the seminar `PolicyIteration` and `ValueIteration` classes. |
| `TicTacToeQLearner.py` | `TicTacToeQLearner`, which keeps the seminar `QLearner` contract of `percept`, `actuate` and `update_episode`, plus a random opponent, a minimax opponent and the evaluation loop. |

The notebook writes its plots to `figures/`, which it creates on the first run.

## Running it

```
pip install numpy matplotlib
jupyter notebook SIT320_D1_TicTacToe_MDP.ipynb
```

Keep the three modules in the same folder as the notebook and run the cells in order.
A full run takes under a minute.

import numpy as np
from functools import lru_cache
from TicTacToeMDP import winner, is_full, legal_moves, AGENT, OPPONENT


class TicTacToeQLearner:
    """
    Tabular Q-learning with the same percept / actuate / update_episode
    contract as the framework's QLearner. The only change is that both the
    exploring move and the greedy move are restricted to legal (empty) cells,
    which the framework never needed because every GridWorld action is legal.
    """

    def __init__(self, num_states, num_actions, legal_actions, alpha=0.2, gamma=0.9,
                 epsilon=0.9, xi=0.99, epsilon_min=0.0):
        self.num_states = num_states
        self.num_actions = num_actions
        self.legal_actions = legal_actions
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon
        self.xi = xi
        self.epsilon_min = epsilon_min
        self.q_table = np.zeros((num_states, num_actions))
        self.visit_count = np.zeros(num_states, dtype=int)
        self.cur_policy = np.zeros(num_states, dtype=int)
        for s in range(num_states):
            moves = legal_actions[s]
            self.cur_policy[s] = np.random.choice(moves) if moves else 0

    def percept(self, s, a, s_prime, r):
        self.visit_count[s] += 1
        moves = self.legal_actions[s_prime]
        q_prime = np.max(self.q_table[s_prime, moves]) if moves else 0.0
        old_q = self.q_table[s, a]
        self.q_table[s, a] = old_q + self.alpha * (r + self.gamma * q_prime - old_q)
        own = self.legal_actions[s]
        self.cur_policy[s] = own[int(np.argmax(self.q_table[s, own]))]

    def actuate(self, s):
        if np.random.uniform() <= self.epsilon:
            return np.random.choice(self.legal_actions[s])
        return self.cur_policy[s]

    def update_episode(self):
        self.epsilon = max(self.epsilon_min, self.epsilon * self.xi)


# ------------------------------------------------------------------ opponents
def random_opponent(board):
    return np.random.choice(legal_moves(board))


@lru_cache(maxsize=None)
def _minimax(board, player):
    """Value of `board` with `player` to move, from O's point of view (+1 O wins)."""
    w = winner(board)
    if w == OPPONENT:
        return 1
    if w == AGENT:
        return -1
    if is_full(board):
        return 0
    results = []
    for m in legal_moves(board):
        nb = list(board)
        nb[m] = player
        results.append(_minimax(tuple(nb), AGENT if player == OPPONENT else OPPONENT))
    return max(results) if player == OPPONENT else min(results)


def minimax_opponent(board):
    """Perfect-play O. Ties broken uniformly at random among equally good moves."""
    best, best_moves = -2, []
    for m in legal_moves(board):
        nb = list(board)
        nb[m] = OPPONENT
        v = _minimax(tuple(nb), AGENT)
        if v > best:
            best, best_moves = v, [m]
        elif v == best:
            best_moves.append(m)
    return np.random.choice(best_moves)


# ----------------------------------------------------------------- evaluation
def play_game(problem, policy, opponent):
    """Agent (X) follows `policy` (state index -> cell) against `opponent`."""
    board = [0] * 9
    while True:
        s = problem.state_index[tuple(board)]
        board[int(policy[s])] = AGENT
        w = winner(board)
        if w == AGENT:
            return 1
        if is_full(board):
            return 0
        board[int(opponent(board))] = OPPONENT
        if winner(board) == OPPONENT:
            return -1


def evaluate(problem, policy, opponent, n=10000):
    """Return (win, draw, loss) rates for `policy` over n games against `opponent`."""
    results = np.array([play_game(problem, policy, opponent) for _ in range(n)])
    return (results == 1).mean(), (results == 0).mean(), (results == -1).mean()

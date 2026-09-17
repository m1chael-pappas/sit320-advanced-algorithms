import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Board cells are indexed 0..8, row-major:
#   0 | 1 | 2
#   3 | 4 | 5
#   6 | 7 | 8
# Cell values: 0 empty, 1 X, 2 O. The learning agent always plays X and always
# moves first. The opponent (O) is part of the environment.

LINES = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
         (0, 3, 6), (1, 4, 7), (2, 5, 8),
         (0, 4, 8), (2, 4, 6)]

AGENT = 1
OPPONENT = 2


def winner(board):
    """Return 1 if X has three in a row, 2 if O has, else 0."""
    for a, b, c in LINES:
        if board[a] != 0 and board[a] == board[b] == board[c]:
            return board[a]
    return 0


def is_full(board):
    return 0 not in board


def legal_moves(board):
    return [i for i in range(9) if board[i] == 0]


def board_to_str(board):
    return ''.join('.XO'[v] for v in board)


class TicTacToeMDP:
    """
    Tic-tac-toe reformulated as a Markov Decision Process from the point of view
    of the X player.

    States      every board that can be reached from the empty board with X to
                move, plus every terminal board (X won, O won, draw) that the
                agent can land on. Boards with O to move are never states: the
                opponent's reply is folded into the transition.
    Actions     the nine cells. Only empty cells are legal in a given state.
    Rewards     +1 on reaching an X win, -1 on reaching an O win, 0 for a draw
                and 0 for every non-terminal transition. Rewards are attached
                to the state the agent lands on, matching the GridWorld
                framework where blackbox_move returns R(s').
    Transitions P(s' | s, a) is 1 when placing X at cell a ends the game.
                Otherwise the opponent chooses uniformly at random among the
                empty cells, so each of the k possible replies has probability
                1 / k. This is the "uniform transition probabilities"
                assumption from the task brief.

    The transition model is stored sparsely as
        self.transitions[s][a] = list of (s_prime, probability)
    because a dense (S, A, S) tensor at S ~ 2700 would be about 500 MB for
    something that is 99.9 percent zeros.
    """

    def __init__(self, gamma=None):
        self.num_actions = 9
        self.states = []            # index -> board tuple
        self.state_index = {}       # board tuple -> index
        self.terminal = []          # index -> bool
        self.reward_function = []   # index -> reward on arrival, R(s)
        self.transitions = {}       # index -> {action: [(s_prime, p), ...]}
        self.legal_actions = {}     # index -> list of legal action indices
        self._build()
        self.num_states = len(self.states)
        self.reward_function = np.array(self.reward_function, dtype=float)
        self.terminal = np.array(self.terminal, dtype=bool)
        self.start_state = self.state_index[tuple([0] * 9)]

    # ------------------------------------------------------------------ build
    def _add_state(self, board):
        board = tuple(board)
        if board in self.state_index:
            return self.state_index[board]
        idx = len(self.states)
        self.states.append(board)
        self.state_index[board] = idx
        w = winner(board)
        if w == AGENT:
            self.terminal.append(True)
            self.reward_function.append(1.0)
        elif w == OPPONENT:
            self.terminal.append(True)
            self.reward_function.append(-1.0)
        elif is_full(board):
            self.terminal.append(True)
            self.reward_function.append(0.0)
        else:
            self.terminal.append(False)
            self.reward_function.append(0.0)
        return idx

    def _build(self):
        """Breadth-first enumeration of every reachable X-to-move state."""
        start = self._add_state([0] * 9)
        frontier = [start]
        seen = {start}
        while frontier:
            s = frontier.pop()
            board = list(self.states[s])
            if self.terminal[s]:
                self.legal_actions[s] = []
                self.transitions[s] = {}
                continue
            moves = legal_moves(board)
            self.legal_actions[s] = moves
            self.transitions[s] = {}
            for a in moves:
                after_x = board.copy()
                after_x[a] = AGENT
                if winner(after_x) == AGENT or is_full(after_x):
                    s_prime = self._add_state(after_x)
                    self.transitions[s][a] = [(s_prime, 1.0)]
                    if s_prime not in seen:
                        seen.add(s_prime)
                        frontier.append(s_prime)
                    continue
                replies = legal_moves(after_x)
                p = 1.0 / len(replies)
                outcomes = []
                for o in replies:
                    after_o = after_x.copy()
                    after_o[o] = OPPONENT
                    s_prime = self._add_state(after_o)
                    outcomes.append((s_prime, p))
                    if s_prime not in seen:
                        seen.add(s_prime)
                        frontier.append(s_prime)
                self.transitions[s][a] = outcomes

    # --------------------------------------------------------------- queries
    def generate_uniform_policy(self):
        """Stochastic policy: equal probability over the legal moves of each state."""
        pi = np.zeros((self.num_states, self.num_actions))
        for s in range(self.num_states):
            moves = self.legal_actions[s]
            if moves:
                pi[s, moves] = 1.0 / len(moves)
        return pi

    def generate_random_policy(self):
        """Deterministic policy: one random legal move per state."""
        policy = np.zeros(self.num_states, dtype=int)
        for s in range(self.num_states):
            moves = self.legal_actions[s]
            policy[s] = np.random.choice(moves) if moves else 0
        return policy

    def summary(self):
        n_term = int(self.terminal.sum())
        n_win = int((self.reward_function == 1.0).sum())
        n_loss = int((self.reward_function == -1.0).sum())
        n_draw = n_term - n_win - n_loss
        n_trans = sum(len(v) for t in self.transitions.values() for v in t.values())
        return {
            'states': self.num_states,
            'non_terminal': self.num_states - n_term,
            'terminal': n_term,
            'x_wins': n_win,
            'o_wins': n_loss,
            'draws': n_draw,
            'nonzero_transitions': n_trans,
        }

    # ----------------------------------------------------- black box for RL
    def reset(self):
        return self.start_state

    def blackbox_move(self, s, a):
        """Same contract as GridWorld.blackbox_move: sample s' and return (s', R(s'))."""
        outcomes = self.transitions[s][a]
        idx = np.random.choice(len(outcomes), p=[p for _, p in outcomes])
        s_prime = outcomes[idx][0]
        return s_prime, self.reward_function[s_prime]

    # --------------------------------------------------------------- plotting
    def plot_board(self, s, ax=None, values=None, policy=None, title=None):
        board = self.states[s]
        own_fig = ax is None
        if own_fig:
            fig, ax = plt.subplots(1, 1, figsize=(3, 3))
        ax.set_xlim(0, 3)
        ax.set_ylim(0, 3)
        ax.set_aspect('equal')
        ax.axis('off')
        for i in range(4):
            ax.plot([i, i], [0, 3], color='black' if i in (0, 3) else 'grey',
                    linestyle='-' if i in (0, 3) else 'dashed', alpha=0.8)
            ax.plot([0, 3], [i, i], color='black' if i in (0, 3) else 'grey',
                    linestyle='-' if i in (0, 3) else 'dashed', alpha=0.8)
        for cell in range(9):
            r, c = divmod(cell, 3)
            x, y = c + 0.5, 2 - r + 0.5
            if board[cell] == AGENT:
                ax.text(x, y, 'X', ha='center', va='center', fontsize=26, color='#1f77b4')
            elif board[cell] == OPPONENT:
                ax.text(x, y, 'O', ha='center', va='center', fontsize=26, color='#d62728')
            elif values is not None:
                ax.text(x, y, f'{values[cell]:.2f}', ha='center', va='center', fontsize=9, color='black')
        if policy is not None and not self.terminal[s]:
            r, c = divmod(int(policy[s]), 3)
            rect = patches.Rectangle((c, 2 - r), 1, 1, edgecolor='none', facecolor='green', alpha=0.25)
            ax.add_patch(rect)
        if title:
            ax.set_title(title, fontsize=9)
        if own_fig:
            plt.tight_layout()
            plt.show()

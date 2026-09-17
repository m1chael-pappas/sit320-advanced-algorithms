import numpy as np
import matplotlib.pyplot as plt


def q_value(problem, values, s, a, gamma):
    """Expected return of taking action a in state s under value estimate `values`."""
    total = 0.0
    for s_prime, p in problem.transitions[s][a]:
        total += p * (problem.reward_function[s_prime] + gamma * values[s_prime])
    return total


class TicTacToePolicyIteration:
    """
    Policy iteration over the sparse tic-tac-toe MDP. Same shape as the
    framework's PolicyIteration (one_policy_evaluation, run_policy_evaluation,
    run_policy_improvement, train) but reads transitions from
    problem.transitions[s][a] instead of a dense tensor, and starts from a
    stochastic policy so the "uniform initial policy" in the brief is taken
    literally.

    self.policy_matrix  (S, A) probabilities, the policy being evaluated
    self.policy         (S,)   greedy action per state after improvement
    """

    def __init__(self, problem, gamma=0.9, init_policy=None):
        self.problem = problem
        self.gamma = gamma
        self.num_states = problem.num_states
        self.num_actions = problem.num_actions
        self.values = np.zeros(self.num_states)
        if init_policy is None:
            self.policy_matrix = problem.generate_uniform_policy()
        else:
            self.policy_matrix = init_policy
        self.policy = np.array([np.argmax(self.policy_matrix[s]) for s in range(self.num_states)])

    def one_policy_evaluation(self):
        delta = 0.0
        for s in range(self.num_states):
            if self.problem.terminal[s]:
                continue
            temp = self.values[s]
            v = 0.0
            for a in self.problem.legal_actions[s]:
                pi = self.policy_matrix[s, a]
                if pi > 0:
                    v += pi * q_value(self.problem, self.values, s, a, self.gamma)
            self.values[s] = v
            delta = max(delta, abs(temp - v))
        return delta

    def run_policy_evaluation(self, tol=1e-3):
        delta_history = []
        while len(delta_history) < 500:
            delta = self.one_policy_evaluation()
            delta_history.append(delta)
            if delta < tol:
                break
        return len(delta_history)

    def run_policy_improvement(self):
        update_policy_count = 0
        for s in range(self.num_states):
            moves = self.problem.legal_actions[s]
            if not moves:
                continue
            temp = self.policy[s]
            q = np.array([q_value(self.problem, self.values, s, a, self.gamma) for a in moves])
            best = moves[int(np.argmax(q))]
            self.policy[s] = best
            self.policy_matrix[s] = 0.0
            self.policy_matrix[s, best] = 1.0
            if temp != best:
                update_policy_count += 1
        return update_policy_count

    def train(self, tol=1e-3, plot=True):
        eval_count_history = []
        policy_change_history = []
        while len(policy_change_history) < 500:
            eval_count = self.run_policy_evaluation(tol)
            policy_change = self.run_policy_improvement()
            eval_count_history.append(eval_count)
            policy_change_history.append(policy_change)
            if policy_change == 0:
                break
        self.eval_count_history = eval_count_history
        self.policy_change_history = policy_change_history

        if plot:
            fig, axes = plt.subplots(2, 1, figsize=(3.5, 4), sharex='all', dpi=200)
            axes[0].plot(np.arange(len(eval_count_history)), eval_count_history, marker='o', markersize=4,
                         alpha=0.7, color='#2ca02c', label='# sweeps in\npolicy evaluation\n' + r'$\gamma =$' + f'{self.gamma}')
            axes[0].legend(fontsize=7)
            axes[1].plot(np.arange(len(policy_change_history)), policy_change_history, marker='o', markersize=4,
                         alpha=0.7, color='#d62728', label='# policy updates in\npolicy improvement\n' + r'$\gamma =$' + f'{self.gamma}')
            axes[1].set_xlabel('Epoch')
            axes[1].legend(fontsize=7)
            plt.tight_layout()
            plt.show()
        return eval_count_history, policy_change_history


class TicTacToeValueIteration:
    """Value iteration over the sparse tic-tac-toe MDP (mirrors ValueIteration)."""

    def __init__(self, problem, gamma=0.9):
        self.problem = problem
        self.gamma = gamma
        self.num_states = problem.num_states
        self.num_actions = problem.num_actions
        self.values = np.zeros(self.num_states)
        self.policy = None

    def one_iteration(self):
        delta = 0.0
        for s in range(self.num_states):
            moves = self.problem.legal_actions[s]
            if not moves:
                continue
            temp = self.values[s]
            best = max(q_value(self.problem, self.values, s, a, self.gamma) for a in moves)
            self.values[s] = best
            delta = max(delta, abs(temp - best))
        return delta

    def get_policy(self):
        pi = np.zeros(self.num_states, dtype=int)
        for s in range(self.num_states):
            moves = self.problem.legal_actions[s]
            if not moves:
                continue
            q = np.array([q_value(self.problem, self.values, s, a, self.gamma) for a in moves])
            ties = [moves[i] for i in range(len(moves)) if np.isclose(q[i], q.max())]
            pi[s] = np.random.choice(ties)
        return pi

    def train(self, tol=1e-3, plot=True):
        delta_history = []
        while True:
            delta = self.one_iteration()
            delta_history.append(delta)
            if delta < tol:
                break
        self.policy = self.get_policy()
        self.delta_history = delta_history

        if plot:
            fig, ax = plt.subplots(1, 1, figsize=(3, 2), dpi=200)
            ax.plot(np.arange(len(delta_history)) + 1, delta_history, marker='o', markersize=4,
                    alpha=0.7, color='#2ca02c', label=r'$\gamma= $' + f'{self.gamma}')
            ax.set_xlabel('Iteration')
            ax.set_ylabel('Delta')
            ax.legend()
            plt.tight_layout()
            plt.show()
        return delta_history

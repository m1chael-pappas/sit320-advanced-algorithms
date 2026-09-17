# SIT320 Advanced Algorithms

Assessment code for SIT320 Advanced Algorithms, one folder per task.
Each folder has a README covering what the task asked for, what the code does and how to run it.

| Folder | Task | Topic |
| --- | --- | --- |
| [`01-introduction`](01-introduction) | 1 | Environment setup, a first Python script, and a minimax tic-tac-toe player |
| [`02-advanced-trees`](02-advanced-trees) | 2, pass | BSTs, rotations, red-black trees, B-trees and B+ trees |
| [`03-advanced-hashing-and-sorting`](03-advanced-hashing-and-sorting) | 3, credit | Extendible hashing bug hunt, and external merge sort |
| [`05-graphs-ii`](05-graphs-ii) | 5, pass | Dijkstra, Bellman-Ford, Floyd-Warshall, Johnson, colouring and bipartiteness |
| [`06-dynamic-programming`](06-dynamic-programming) | 6, pass | Staircase, longest common subsequence, knapsack and coin change |
| [`07-greedy-algorithms`](07-greedy-algorithms) | 7, pass | Huffman coding, Prim's algorithm, and where greedy coin change fails |
| [`08-linear-programming`](08-linear-programming) | 8, pass | LU decomposition, the graphical method and simplex |
| [`09-network-flow-algorithms`](09-network-flow-algorithms) | 9 | Karger's minimum cut and Ford-Fulkerson maximum flow |
| [`10-ai-algorithms`](10-ai-algorithms) | D1, distinction | Tic-tac-toe as an MDP, solved with dynamic programming and learned with Q-learning |

Task 4, Advanced Algorithmic Complexity, was a written submission and has no code.

## Running anything here

Every task is a Jupyter notebook that runs top to bottom.

```
pip install numpy matplotlib graphviz
```

The `graphviz` Python package draws the trees and graphs in tasks 2, 5, 6 and 7, and it needs the Graphviz binaries installed too, through `apt install graphviz` or `brew install graphviz`.
Each folder's README lists what that task needs on its own.

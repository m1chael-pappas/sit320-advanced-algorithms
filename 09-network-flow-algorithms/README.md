# Network flow algorithms

SIT320 task 9.

Randomised minimum cut and maximum flow.
No template was provided for this module, so all of the code is my own.
Ford-Fulkerson follows CLRS chapter 26, and the Programiz page linked in the task sheet was the reference for the adjacency-matrix layout.

## What the notebook covers

| Section | Contents |
| --- | --- |
| 1 | Karger's algorithm for global minimum cut on unweighted graphs. |
| 2 | Extending Karger to weighted graphs, by contracting edges with probability proportional to weight. |
| 3 | Ford-Fulkerson on the seminar network, giving maximum flow and the minimum s-t cut that certifies it. |

Karger is randomised and can return a cut that is not minimum, so it is run repeatedly and the best result kept.
Ford-Fulkerson is exact, and the max-flow min-cut theorem is what connects the two halves.

## Running it

```
pip install numpy matplotlib
jupyter notebook Code_NetworkAlgorithms.ipynb
```

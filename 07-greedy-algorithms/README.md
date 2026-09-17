# Greedy algorithms

SIT320 pass task 7.

Where taking the locally best option is provably right, and where it is not.

## What the notebook covers

| Activity | Contents |
| --- | --- |
| 1 | Huffman prefix tree for an arbitrary distribution, run on [A:45, B:13, C:12, D:16, E:9, F:5]. |
| 2 | Prim's algorithm for a minimum spanning tree, first the straightforward version from the lab and then an efficient one, timed against each other on large random graphs. |
| 3 | Greedy coin change against the dynamic programming solution, and the coin systems where greedy gives the wrong answer. |

Activity 3 is the counterexample to the other two.
Huffman and Prim are greedy and optimal, greedy coin change is neither in general.

## Files

`graph.py` is the unit's graph library, holding the `Node` and graph classes the notebook imports with `from graph import *`.

## Running it

```
pip install numpy graphviz
jupyter notebook Code_Greedy.ipynb
```

Keep `graph.py` in the same folder as the notebook.
The `graphviz` Python package needs the Graphviz binaries installed as well, through `apt install graphviz` or `brew install graphviz`.

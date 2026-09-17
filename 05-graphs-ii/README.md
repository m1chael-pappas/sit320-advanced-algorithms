# Graphs II

SIT320 pass task 5.
Covers the Graphs I and Graphs II material together.

Shortest path algorithms across the cases that break each other, plus two colouring problems.
The written reflection for each task is in the accompanying report.

## What the notebook covers

| Task | Contents |
| --- | --- |
| 1 | Graph preliminaries and Dijkstra, from the lab sections |
| 2 | Graph colouring |
| 3 | Testing whether a graph is bipartite |
| 4 | Bellman-Ford, which handles the negative edges Dijkstra cannot |
| 5 | Floyd-Warshall for all pairs |
| 6 | Johnson's algorithm, with a timed comparison against Floyd-Warshall |

Johnson's reweighting step is what lets it run Dijkstra on a graph with negative edges, and the comparison at the end shows where its advantage over Floyd-Warshall appears.

## Running it

```
pip install numpy graphviz
jupyter notebook code_2.ipynb
```

The `graphviz` Python package needs the Graphviz binaries installed as well, through `apt install graphviz` or `brew install graphviz`.

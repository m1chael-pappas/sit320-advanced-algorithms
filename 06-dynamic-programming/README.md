# Dynamic programming

SIT320 pass task 6.

Four problems solved by finding the recurrence first and then deciding how to store it.

## What the notebook covers

| Activity | Contents |
| --- | --- |
| 1 | Staircase with hops of 1, 2 or 3 steps. Count the ways to climb n steps. |
| 2 | Longest common subsequence, printing the full C matrix and the subsequence itself. |
| 3 | 0/1 knapsack, including a space-optimised version that keeps one row and walks the capacity loop backwards. |
| 4 | Minimum coins to make a given amount. |

The knapsack section explains why the single-row version has to iterate capacity in reverse: during pass j, cells at or above the current capacity already hold row j while the cells below still hold row j-1.

Activity 4 also works through what breaks when -1 is used as the sentinel inside the recurrence instead of infinity, with the two failure modes depending on how the recurrence is written.

## Running it

```
pip install numpy graphviz
jupyter notebook code.ipynb
```

The `graphviz` Python package needs the Graphviz binaries installed as well, through `apt install graphviz` or `brew install graphviz`.
